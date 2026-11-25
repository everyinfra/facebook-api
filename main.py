"""Facebook API 示例（Facebook API in Python）。

  python main.py page "https://www.facebook.com/NASA" --out page.json  # 公开主页资料 / page profile
  python main.py posts "https://www.facebook.com/NASA" --out posts.csv # 主页帖子 / page posts
  python main.py post "<帖子链接>" --out post.json                     # 单条帖子 / one post
  python main.py comments "<帖子链接>" --out comments.csv              # 帖子评论 / comments
"""
import argparse

from everyinfra import fetch, report


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    pa = sub.add_parser("page", help="公开主页资料 / public page profile")
    pa.add_argument("url")
    po = sub.add_parser("posts", help="主页帖子 / a page's posts")
    po.add_argument("url")
    pos = sub.add_parser("post", help="单条帖子 / one post")
    pos.add_argument("url")
    c = sub.add_parser("comments", help="帖子评论 / comments of one post")
    c.add_argument("url")
    for x in (pa, po, pos, c):
        x.add_argument("--out", help="存成 .csv 或 .json / write .csv or .json")
    a = p.parse_args()

    if a.cmd == "page":
        rows, charged = fetch("profile", {"url": a.url})
    elif a.cmd == "posts":
        rows, charged = fetch("user_posts", {"url": a.url})
    elif a.cmd == "post":
        rows, charged = fetch("post", {"url": a.url})
    else:
        rows, charged = fetch("comments", {"url": a.url})
    report(rows, charged, a.out)


if __name__ == "__main__":
    main()
