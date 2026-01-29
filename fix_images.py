import os
import re
from pathlib import Path


def fix_obsidian_images(repo_path="."):
    """
    只修改 ceshi 文件夹里的 markdown 文件
    图片已手动复制到 images/ 文件夹
    """
    repo_path = Path(repo_path).resolve()
    images_dir = repo_path / "images"

    # 检查 images 文件夹
    if not images_dir.exists():
        print(f"⚠️ 请先创建 {images_dir} 文件夹，并把图片复制进去")
        return

    # 获取所有图片文件名
    image_files = {f.name for f in images_dir.iterdir() if f.is_file()}
    print(f"images 文件夹里有 {len(image_files)} 个文件")

    stats = {
        "md_files": 0,
        "links_fixed": 0,
        "images_not_found": []
    }

    # 处理所有 markdown 文件
    for md_file in repo_path.rglob("*.md"):
        if md_file.name == "fix_images.py":
            continue

        stats["md_files"] += 1
        content = md_file.read_text(encoding='utf-8')
        original_content = content

        # 匹配 Obsidian 格式：![[Pasted image 20250717094529.png]]
        # 支持：![[图片名]]、![[图片名|描述]]、![[图片名#大小]]
        pattern = r'!\[\[([^|\]#\n]+?)(?:[|\]#][^\]]*)?\]\]'

        def replace_link(match):
            image_name = match.group(1).strip()

            # 检查图片是否存在（支持空格和 %20）
            found = False
            if image_name in image_files:
                found = True
            elif image_name.replace('%20', ' ') in image_files:
                image_name = image_name.replace('%20', ' ')
                found = True

            if found:
                # 转成 URL 编码（空格变 %20）
                url_name = image_name.replace(' ', '%20')
                stats["links_fixed"] += 1
                return f'![{image_name}](./images/{url_name})'
            else:
                # 图片没找到，记录并保留占位
                if image_name not in stats["images_not_found"]:
                    stats["images_not_found"].append(image_name)
                    print(f"⚠️ 未找到图片: {image_name}")
                # 仍然替换格式，但路径可能不对
                url_name = image_name.replace(' ', '%20')
                return f'![{image_name}](./images/{url_name})'

        # 执行替换
        new_content = re.sub(pattern, replace_link, content)

        # 保存（只有变化了才保存）
        if new_content != original_content:
            md_file.write_text(new_content, encoding='utf-8')
            print(f"✅ 已修复: {md_file.name}")

    # 输出报告
    print("\n" + "=" * 50)
    print("处理完成！")
    print(f"扫描文件: {stats['md_files']}")
    print(f"修复链接: {stats['links_fixed']}")
    if stats["images_not_found"]:
        print(f"\n⚠️ 未找到的图片 ({len(stats['images_not_found'])}):")
        for name in stats["images_not_found"][:5]:
            print(f"  - {name}")
        if len(stats["images_not_found"]) > 5:
            print(f"  ... 还有 {len(stats['images_not_found']) - 5} 个")
        print("\n请把这些图片手动复制到 images/ 文件夹")
    print("=" * 50)
    print("\nObsidian 原文件未被修改，放心！")


if __name__ == "__main__":
    fix_obsidian_images()