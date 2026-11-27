const NOT_FOUND_MARKDOWN = `# Page not found

There is no page at this URL on repalis.com.

Repalis is a payment infrastructure and Merchant of Record for software companies. These pages are a good place to continue:

- [Documentation](https://repalis.com/docs)
- [Documentation index for LLMs](https://repalis.com/llms.txt)
- [API reference](https://repalis.com/docs/api-reference/introduction)
- [Sitemap](https://repalis.com/sitemap.xml)
- [Homepage](https://repalis.com)
`

export function GET() {
  return new Response(NOT_FOUND_MARKDOWN, {
    status: 404,
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      Vary: 'Accept',
    },
  })
}
