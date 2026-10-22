from app.utils.css_builder import CssBuilder
from app.utils.html_converter import HtmlConverter

# テストデータ
sample_md = """
# コーヒー豆の在庫管理システム

これは **HtmlConverter** と **CssBuilder** の連携テスト用テキストです。

## 今日の焙煎リスト
- 東ティモール（深煎り）
- コスタリカ（中深煎り）
- *グアテマラ*（中煎り）

### 注意事項
1. 在庫が **50g** を切ったら自動アラートを出す
2. 淹れるたびに `use()` メソッドで更新する

> **Note:** スタイルが適用された完全なHTMLとして生成されます。
"""

# 1. スタイル設定の初期化（コーヒー系のカラー）
css_builder = CssBuilder(primary_color="#4A2E10", bg_color="#FDFBF7")

# 2. コンバーターのインスタンス化
converter = HtmlConverter(sample_md)

# 3. 完全なHTMLドキュメントの文字列を取得（ファイル保存にそのまま使える）
full_html_code = converter.build_full_document(
    title="在庫レポート", css_builder=css_builder, pretty=True
)

print(full_html_code)