#!/usr/bin/env bash
# Facebook API 的 curl 示例：所有能力都发到同一个地址，只换 action 和 params。
# curl examples for the Facebook API: every capability uses the same URL; only action and params change.
#
#   export EVERYINFRA_API_KEY=<your API key>
#   bash examples/curl.sh profile https://www.facebook.com/NASA
#   bash examples/curl.sh user_posts https://www.facebook.com/NASA # 公开主页链接 / a public page link
#   bash examples/curl.sh post "<post url>"                        # posts 结果里的 url / the url from a posts result
#   bash examples/curl.sh comments "<post url>"                    # posts 结果里的 url / the url from a posts result
set -euo pipefail
: "${EVERYINFRA_API_KEY:?Set EVERYINFRA_API_KEY first: https://everyinfra.com/docs#quickstart}"
action=${1:?"usage: bash examples/curl.sh <profile|user_posts|post|comments> <value>"}
value=${2:?"value: a page url or a post url"}

case "$action" in
  profile | user_posts | post | comments) params="{\"url\":\"$value\"}" ;;
  *) echo "unknown action: $action (use profile, user_posts, post or comments)" >&2; exit 2 ;;
esac

curl -sS -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"platform\":\"facebook\",\"action\":\"$action\",\"params\":$params}"
echo
