#!/usr/bin/env python3
"""Bağımsız (yalnızca Python standart kütüphanesi) Markdown -> DOCX dönüştürücü.

Hukuk Asistanı eklentisinin ürettiği .md çıktılarını, ek bir kütüphane
kurulumu (pandoc, python-docx vb.) gerektirmeden Word'de düzgün açılan bir
.docx ikizine çevirir. Yalnızca bu eklentinin kendi çıktılarında kullandığı
sınırlı markdown alt kümesini destekler: başlık (#/##/###), kalın
(**metin**), eğik (*metin*), satır içi kod (`metin`), madde listesi
(- veya *), numaralı liste (1.), alıntı (>), yatay çizgi (---) ve
GitHub-stili tablolar (| ... |).

Kullanım:
    python3 md_to_docx.py girdi.md cikti.docx
"""
import re
import sys
import zipfile
from xml.sax.saxutils import escape as _esc

NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def parse_inline(text):
    """Metni (metin, {bold, italic, code}) parça listesine ayırır."""
    runs = []
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            runs.append((part[2:-2], {"bold": True}))
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            runs.append((part[1:-1], {"code": True}))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            runs.append((part[1:-1], {"italic": True}))
        else:
            runs.append((part, {}))
    return runs or [(text, {})]


def xml_run(text, bold=False, italic=False, code=False):
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if code:
        props.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>')
        props.append('<w:shd w:val="clear" w:fill="F2F2F2"/>')
    rpr = "<w:rPr>" + "".join(props) + "</w:rPr>" if props else ""
    return (
        "<w:r>"
        + rpr
        + '<w:t xml:space="preserve">'
        + _esc(text)
        + "</w:t></w:r>"
    )


def xml_runs(text):
    return "".join(xml_run(t, **f) for t, f in parse_inline(text))


def xml_paragraph(text="", style=None, indent=None, align=None, border=False):
    ppr = []
    if style:
        ppr.append('<w:pStyle w:val="%s"/>' % style)
    if align:
        ppr.append('<w:jc w:val="%s"/>' % align)
    if indent:
        ppr.append('<w:ind w:left="%d"/>' % indent)
    if border:
        ppr.append(
            '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" '
            'w:color="BFBFBF"/></w:pBdr>'
        )
    pprxml = "<w:pPr>" + "".join(ppr) + "</w:pPr>" if ppr else ""
    body = xml_runs(text) if text else ""
    return "<w:p>" + pprxml + body + "</w:p>"


def xml_table(rows):
    borders = (
        "<w:tblBorders>"
        + "".join(
            '<w:%s w:val="single" w:sz="4" w:space="0" w:color="999999"/>' % s
            for s in ("top", "left", "bottom", "right", "insideH", "insideV")
        )
        + "</w:tblBorders>"
    )
    tblpr = "<w:tblPr>" + borders + '<w:tblW w:w="0" w:type="auto"/></w:tblPr>'
    trs = []
    for row in rows:
        tcs = []
        for cell in row:
            tcs.append(
                "<w:tc><w:tcPr><w:tcMar>"
                '<w:top w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/>'
                '<w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/>'
                "</w:tcMar></w:tcPr>"
                + xml_paragraph(cell)
                + "</w:tc>"
            )
        trs.append("<w:tr>" + "".join(tcs) + "</w:tr>")
    return "<w:tbl>" + tblpr + "".join(trs) + "</w:tbl>"


TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def parse_blocks(md_text):
    lines = md_text.replace("\r\n", "\n").split("\n")
    blocks = []
    i = 0
    n = len(lines)
    para_buf = []

    def flush_para():
        if para_buf:
            blocks.append(("para", " ".join(para_buf).strip()))
            para_buf.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_para()
            i += 1
            continue

        m = re.match(r"^(#{1,3})\s+(.*)$", stripped)
        if m:
            flush_para()
            blocks.append(("heading", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            flush_para()
            blocks.append(("hr",))
            i += 1
            continue

        if (
            "|" in stripped
            and i + 1 < n
            and TABLE_SEP_RE.match(lines[i + 1].strip())
        ):
            flush_para()
            header = split_table_row(stripped)
            rows = [header]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_table_row(lines[i]))
                i += 1
            blocks.append(("table", rows))
            continue

        m = re.match(r"^[-*]\s+(.*)$", stripped)
        if m:
            flush_para()
            blocks.append(("bullet", m.group(1).strip()))
            i += 1
            continue

        m = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if m:
            flush_para()
            blocks.append(("numbered", m.group(1).strip()))
            i += 1
            continue

        if stripped.startswith(">"):
            flush_para()
            blocks.append(("quote", stripped.lstrip(">").strip()))
            i += 1
            continue

        para_buf.append(stripped)
        i += 1

    flush_para()
    return blocks


def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "heading":
            level = min(b[1], 3)
            out.append(xml_paragraph(b[2], style="Heading%d" % level))
        elif kind == "para":
            out.append(xml_paragraph(b[1]))
        elif kind == "bullet":
            out.append(xml_paragraph("• " + b[1], style="ListParagraph", indent=360))
        elif kind == "numbered":
            out.append(xml_paragraph(b[1], style="ListParagraph", indent=360))
        elif kind == "quote":
            out.append(xml_paragraph(b[1], style="Quote", indent=360))
        elif kind == "hr":
            out.append(xml_paragraph("", border=True))
        elif kind == "table":
            out.append(xml_table(b[1]))
            out.append(xml_paragraph(""))
    return "".join(out)


DOCUMENT_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:document %s>' % NS
    + "<w:body>%s"
    + "<w:sectPr>"
    '<w:pgSz w:w="11907" w:h="16840"/>'
    '<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417" '
    'w:header="708" w:footer="708" w:gutter="0"/>'
    "</w:sectPr>"
    "</w:body></w:document>"
)

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr><w:spacing w:after="160" w:line="276" w:lineRule="auto"/></w:pPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="32"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="200" w:after="100"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="27"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="160" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Quote">
    <w:name w:val="Quote"/><w:basedOn w:val="Normal"/>
    <w:rPr><w:i/><w:color w:val="595959"/></w:rPr>
  </w:style>
</w:styles>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>"""

RELS_ROOT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>"""

RELS_DOCUMENT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

CORE_PROPS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <dc:creator>Hukuk Asistanı</dc:creator>
  <dc:title>%s</dc:title>
</cp:coreProperties>"""


def convert(md_text, title="Belge"):
    blocks = parse_blocks(md_text)
    body = render_blocks(blocks)
    document_xml = DOCUMENT_TEMPLATE % body
    return document_xml, STYLES_XML, CORE_PROPS % _esc(title)


def write_docx(out_path, document_xml, styles_xml, core_xml):
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS_ROOT)
        z.writestr("docProps/core.xml", core_xml)
        z.writestr("word/document.xml", document_xml)
        z.writestr("word/styles.xml", styles_xml)
        z.writestr("word/_rels/document.xml.rels", RELS_DOCUMENT)


def main(argv):
    if len(argv) != 3:
        sys.stderr.write("Kullanim: md_to_docx.py girdi.md cikti.docx\n")
        return 2
    src, dst = argv[1], argv[2]
    try:
        with open(src, "r", encoding="utf-8") as f:
            md_text = f.read()
    except OSError as e:
        sys.stderr.write("Girdi okunamadi: %s\n" % e)
        return 1

    title = dst.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    document_xml, styles_xml, core_xml = convert(md_text, title=title)
    try:
        write_docx(dst, document_xml, styles_xml, core_xml)
    except OSError as e:
        sys.stderr.write("Cikti yazilamadi: %s\n" % e)
        return 1

    print("OK: %s" % dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
