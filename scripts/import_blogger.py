#!/usr/bin/env python3
"""Import Blogger posts from Google Takeout Atom feed into Hugo content."""

import xml.etree.ElementTree as ET
import os
import re

FEED_PATH = "Takeout/Blogger/Blogs/EricDaugherty.com/feed.atom"
OUTPUT_DIR = "content/posts"
NS = {
    'atom': 'http://www.w3.org/2005/Atom',
    'blogger': 'http://schemas.google.com/blogger/2018',
}


def slugify(text):
    """Convert text to a URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')


def main():
    tree = ET.parse(FEED_PATH)
    root = tree.getroot()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    count = 0
    for entry in root.findall('atom:entry', NS):
        entry_type = entry.find('blogger:type', NS)
        if entry_type is None or entry_type.text != 'POST':
            continue
        status = entry.find('blogger:status', NS)
        if status is None or status.text != 'LIVE':
            continue

        title_el = entry.find('atom:title', NS)
        title = title_el.text if title_el is not None and title_el.text else 'Untitled'

        published_el = entry.find('atom:published', NS)
        published = published_el.text if published_el is not None else ''

        content_el = entry.find('atom:content', NS)
        content = content_el.text if content_el is not None and content_el.text else ''

        filename_el = entry.find('blogger:filename', NS)
        url_path = filename_el.text if filename_el is not None and filename_el.text else ''

        # Derive slug from blogger:filename or title
        if url_path:
            slug = url_path.rstrip('/').split('/')[-1]
            if slug.endswith('.html'):
                slug = slug[:-5]
        else:
            slug = slugify(title)

        date_str = published[:10] if published else '1970-01-01'

        # Escape title for YAML front matter
        safe_title = title.replace('\\', '\\\\').replace('"', '\\"')

        lines = [
            '---',
            f'title: "{safe_title}"',
            f'date: {published}',
        ]
        if url_path:
            lines.append(f'url: {url_path}')
        lines.append('draft: false')
        lines.append('---')
        lines.append('')
        lines.append(content)
        lines.append('')

        out_path = os.path.join(OUTPUT_DIR, f"{date_str}-{slug}.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        count += 1

    print(f"Exported {count} posts to {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
