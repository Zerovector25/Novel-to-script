import streamlit as st

st.set_page_config(
    page_title="AI 小说转剧本工具",
    page_icon="🎬",
    layout="wide",
)

st.title("AI 小说转剧本工具")

st.write(
    "这是一个帮助小说作者把小说文本转换成结构化 YAML 剧本初稿的工具。"
)

novel_text = st.text_area(
    "请粘贴小说文本",
    height=300,
    placeholder="请粘贴至少 3 个章节的小说文本，例如：第一章、第二章、第三章……",
)

if st.button("生成剧本"):
    if novel_text.strip() == "":
        st.warning("请先输入小说文本。")
    else:
        st.success("已收到小说文本。下一步会加入章节检测和剧本生成。")
        st.code(
            """
script:
  title: "示例剧本"
  scenes:
    - id: "scene_001"
      location: "待生成"
      summary: "这里将显示 AI 生成的剧本内容"
""",
            language="yaml",
        )
