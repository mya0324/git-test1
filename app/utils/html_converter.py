"""MarkdownテキストをカスタムHTMLへ変換およびプレビュー表示するモジュール。"""

import markdown
from bs4 import BeautifulSoup
from IPython.display import HTML

from app.utils.css_builder import CssBuilder


class HtmlConverter:
    """Markdownテキストを受け取り、独自のクラスやタグ構造を組み込んだカスタムHTMLに変換するクラス。

    Attributes:
        raw_text (str): 変換対象となる生のMarkdownテキスト。
    """

    def __init__(self, raw_text: str):
        self.raw_text = raw_text

    def convert(self, pretty: bool = False) -> str:
        """Markdownフラグメント（divの要素部分のみ）をHTML化して返す。"""
        base_html = markdown.markdown(self.raw_text, extensions=["extra"])
        custom_html = base_html.replace("<h1>", '<h1 class="custom-heading">')
        full_html = f'<div class="content-box">\n{custom_html}\n</div>'

        if pretty:
            soup = BeautifulSoup(full_html, "html.parser")
            return soup.prettify()

        return full_html

    def build_full_document(
        self,
        title: str = "コーヒー豆在庫レポート",
        css_builder: CssBuilder = None,
        pretty: bool = False,
    ) -> str:
        """CssBuilderと連携し、完全なHTMLドキュメント（<!DOCTYPE html>...）を生成する。

        Args:
            title (str): HTMLページのタイトル。
            css_builder (CssBuilder, optional): スタイル生成用オブジェクト。未指定時はデフォルトを生成。
            pretty (bool): Trueの場合、HTML全体を整形して返す。

        Returns:
            str: 完全なHTMLドキュメント文字列。
        """
        if css_builder is None:
            css_builder = CssBuilder()

        css_text = css_builder.build()
        body_content = self.convert(pretty=False)

        full_doc = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css_text}
    </style>
</head>
<body>
{body_content}
</body>
</html>"""

        if pretty:
            soup = BeautifulSoup(full_doc, "html.parser")
            return soup.prettify()

        return full_doc

    def preview(self, title: str = "コーヒー豆在庫レポート") -> HTML:
        """Colab等の画面上でスタイル付きプレビューを表示可能なHTMLオブジェクトを返す。"""
        full_html = self.build_full_document(title=title, pretty=False)
        return HTML(full_html)