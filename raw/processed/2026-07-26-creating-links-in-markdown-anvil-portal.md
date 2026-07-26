# Creating Links in Markdown — AnVIL Portal

source_url: https://anvilproject.org/guides/content/creating-links

---

Markdown links use square brackets for text and parentheses for the URL:

`[Link text Here](https://link-url-here.org)`

**Internal Links** (within AnVIL portal) follow these rules:
- Use relative paths, omitting protocol and domain (e.g., `"/guides/content/creating-links"`)
- Use the page's site `path`, not the file's repository location
- Omit the `.md` suffix
- Always begin with a forward slash `/`

Example: `[An Internal Link](/guides/content/editing-an-existing-page)`

**Linking to Headings:** Hover over any heading to reveal a link icon. Click it, copy the URL from the address bar, strip the domain, and use the resulting relative URL with an `#anchor` fragment.

**External Links** use the same syntax but with the full URL:

`[This is an external link to genome.gov](https://www.genome.gov/)`
