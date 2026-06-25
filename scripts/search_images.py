#!/usr/bin/env python3
"""图片搜索下载工具 - 无需API Key
支持: Bing、Google、Pixabay(需免费Key)
用法: python search_images.py "关键词" --source bing --limit 15 --outdir ./images
"""

import argparse, os, sys, time
from pathlib import Path

def search_bing(keyword, limit=15, outdir=".", min_width=800):
    """Bing 图片搜索（无需API Key）"""
    from icrawler.builtin import BingImageCrawler
    outdir = str(Path(outdir).resolve())
    os.makedirs(outdir, exist_ok=True)

    filters = {}
    if min_width:
        filters["size"] = "large"

    downloaded = []
    crawler = BingImageCrawler(
        storage={"root_dir": outdir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
    )

    def on_done():
        pass

    # Set up download tracking
    original_download = crawler.downloader.download
    def tracked_download(task, *args, **kwargs):
        result = original_download(task, *args, **kwargs)
        if result:
            downloaded.append(result)

    crawler.downloader.download = tracked_download
    crawler.crawl(keyword=keyword, filters=filters, max_num=limit)

    # List downloaded files
    files = list(Path(outdir).glob("*.[jp][np][g]")) + list(Path(outdir).glob("*.jpeg")) + list(Path(outdir).glob("*.webp"))
    return [str(f) for f in files]

def search_google(keyword, limit=15, outdir=".", min_width=800):
    """Google 图片搜索（无需API Key，但可能被限速）"""
    from icrawler.builtin import GoogleImageCrawler
    outdir = str(Path(outdir).resolve())
    os.makedirs(outdir, exist_ok=True)

    filters = {}
    if min_width:
        filters["size"] = "large"

    crawler = GoogleImageCrawler(
        storage={"root_dir": outdir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
    )
    crawler.crawl(keyword=keyword, filters=filters, max_num=limit)

    files = list(Path(outdir).glob("*.[jp][np][g]")) + list(Path(outdir).glob("*.jpeg")) + list(Path(outdir).glob("*.webp"))
    return [str(f) for f in files]

def search_pixabay(keyword, limit=15, outdir=".", api_key=None):
    """Pixabay 搜索（需免费API Key: https://pixabay.com/api/docs/）"""
    import requests
    api_key = api_key or os.environ.get("PIXABAY_API_KEY", "")
    if not api_key:
        print("[Pixabay] No API key. Get free key at https://pixabay.com/api/docs/")
        return []

    url = "https://pixabay.com/api/"
    params = {
        "key": api_key,
        "q": keyword,
        "image_type": "photo",
        "per_page": min(limit, 200),
        "safesearch": "true",
    }
    resp = requests.get(url, params=params, timeout=15)
    data = resp.json()

    outdir = Path(outdir).resolve()
    os.makedirs(outdir, exist_ok=True)
    downloaded = []

    for i, hit in enumerate(data.get("hits", [])[:limit]):
        img_url = hit.get("largeImageURL") or hit.get("webformatURL")
        if not img_url:
            continue
        try:
            img_data = requests.get(img_url, timeout=15).content
            ext = os.path.splitext(img_url.split("?")[0])[1] or ".jpg"
            fname = outdir / f"pixabay_{hit['id']}{ext}"
            with open(fname, "wb") as f:
                f.write(img_data)
            downloaded.append(str(fname))
        except Exception as e:
            print(f"  skip {hit['id']}: {e}")

    return downloaded

def main():
    parser = argparse.ArgumentParser(description="图片搜索下载")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("--source", choices=["bing","google","pixabay","all"], default="bing", help="图片来源")
    parser.add_argument("--limit", type=int, default=15, help="下载数量")
    parser.add_argument("--outdir", default=".", help="输出目录")
    parser.add_argument("--min-width", type=int, default=800, help="最小图片宽度")
    parser.add_argument("--pixabay-key", help="Pixabay API Key")
    args = parser.parse_args()

    sources = ["bing", "google"] if args.source == "all" else [args.source]
    all_files = []

    for src in sources:
        try:
            if src == "bing":
                files = search_bing(args.keyword, args.limit, args.outdir, args.min_width)
            elif src == "google":
                files = search_google(args.keyword, args.limit, args.outdir, args.min_width)
            elif src == "pixabay":
                files = search_pixabay(args.keyword, args.limit, args.outdir, args.pixabay_key)
            all_files.extend(files)
            print(f"[{src}] Found {len(files)} images")
        except Exception as e:
            print(f"[{src}] Error: {e}")

    print(f"\nTotal: {len(all_files)} images saved to {args.outdir}")
    for f in all_files[:5]:
        print(f"  {f}")
    if len(all_files) > 5:
        print(f"  ... and {len(all_files)-5} more")

if __name__ == "__main__":
    main()
