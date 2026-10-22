"""CSSの自動生成を行うユーティリティモジュール。"""


class CssBuilder:
    """レイアウト崩れを防ぐための基本CSSスタイルを動的に生成するクラス。

    Attributes:
        primary_color (str): 基本となるテキスト・テーマカラー。
        font_size (str): 基本フォントサイズ。
        bg_color (str): 背景色。
    """

    def __init__(
        self,
        primary_color: str = "#4A2E10",
        font_size: str = "16px",
        bg_color: str = "#FDFBF7",
    ):
        self.primary_color = primary_color
        self.font_size = font_size
        self.bg_color = bg_color

    def build(self) -> str:
        """CSSスケルトン文字列を生成して返す。"""
        css_skeleton = f"""/* --- Auto-generated CSS Skeleton --- */
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: {self.font_size};
    color: #333333;
    line-height: 1.6;
    background-color: {self.bg_color};
    padding: 20px;
}}

.content-box {{
    max-width: 800px;
    margin: 0 auto;
    background: #ffffff;
    padding: 32px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}}

.custom-heading {{
    color: {self.primary_color};
    border-bottom: 2px solid {self.primary_color};
    padding-bottom: 8px;
    margin-bottom: 16px;
}}

h2, h3 {{
    color: {self.primary_color};
    margin-top: 20px;
    margin-bottom: 10px;
}}

ul, ol {{
    margin-left: 20px;
    margin-bottom: 16px;
}}

li {{
    margin-bottom: 4px;
}}

code {{
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: monospace;
}}

blockquote {{
    border-left: 4px solid {self.primary_color};
    padding-left: 12px;
    color: #666666;
    margin: 16px 0;
    background-color: #f9f9f9;
    padding-top: 8px;
    padding-bottom: 8px;
}}
"""
        return css_skeleton.strip()