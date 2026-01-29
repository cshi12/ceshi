import os
import re
import shutil
from pathlib import Path


def sync_from_obsidian():
    """
    只从 Obsidian 的【测试】文件夹同步
    """
    # 路径配置 - 只改这里！
    obsidian_test_path = Path(r"D:\hao的java笔记\hao\测试")  # 只同步测试文件夹
    obsidian_picture_path = Path(r"D:\hao的java笔记\hao\picture")  # 图片还在这里
    ceshi_path = Path(r"D:\我的GitHub库\ceshi")  # GitHub仓库

    images_dir = ceshi_path / "images"
    images_dir.mkdir(exist_ok=True)

    # 统计
    stats = {
        "new_md_files": [],
        "updated_md_files": [],
        "new_images": [],
        "skipped_images": [],
        "not_found_images": []
    }

    # 获取 ceshi 已有的文件
    existing_md = {f.name for f in ceshi_path.glob("*.md")
                   if f.name not in ["fix_images.py", "sync_from_obsidian.py"]}
    existing_images = {f.name for f in images_dir.iterdir() if f.is_file()}

    print(f"已有 Markdown: {len(existing_md)} 个")
    print(f"已有图片: {len(existing_images)} 个")
    print(f"只同步: {obsidian_test_path}")
    print("=" * 50)

    # 支持的图片格式
    image_exts = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'}

    # 第一步：只找【测试】文件夹里的 .md 文件
    obsidian_md_files = list(obsidian_test_path.glob("*.md"))
    print(f"扫描到测试笔记: {len(obsidian_md_files)} 个")

    for md_file in obsidian_md_files:
        file_name = md_file.name

        if file_name in ["fix_images.py", "sync_from_obsidian.py"]:
            continue

        target_file = ceshi_path / file_name

        # 检查是否需要复制
        need_copy = False
        if file_name not in existing_md:
            need_copy = True
            stats["new_md_files"].append(file_name)
            print(f"🆕 新笔记: {file_name}")
        else:
            # 对比修改时间
            obsidian_mtime = md_file.stat().st_mtime
            ceshi_mtime = target_file.stat().st_mtime

            if obsidian_mtime > ceshi_mtime + 60:
                need_copy = True
                stats["updated_md_files"].append(file_name)
                print(f"📝 更新: {file_name}")

        if need_copy:
            # 复制 .md 文件
            shutil.copy2(str(md_file), str(target_file))

            # 分析引用的图片
            content = md_file.read_text(encoding='utf-8')
            pattern = r'!\[\[([^|\]#\n]+?)(?:[|\]#][^\]]*)?\]\]'
            matches = re.findall(pattern, content)

            for img_name in matches:
                img_name = img_name.strip()

                # 跳过 canvas 文件
                if img_name.endswith('.canvas'):
                    print(f"  ⚠️ 跳过 canvas: {img_name}")
                    continue

                # 在 picture 文件夹找图片
                img_found = False
                for ext in [''] + list(image_exts):
                    search_name = img_name if ext == '' else img_name + ext
                    img_path = obsidian_picture_path / search_name

                    if img_path.exists():
                        img_found = True

                        if search_name in existing_images:
                            stats["skipped_images"].append(search_name)
                            print(f"  ⏭️ 跳过: {search_name}")
                        else:
                            dst_path = images_dir / search_name
                            shutil.copy2(str(img_path), str(dst_path))
                            existing_images.add(search_name)
                            stats["new_images"].append(search_name)
                            print(f"  ✅ 复制: {search_name}")
                        break

                if not img_found:
                    stats["not_found_images"].append(img_name)
                    print(f"  ❌ 找不到: {img_name}")

    # 修复所有 .md 文件的路径
    print("\n" + "=" * 50)
    print("正在修复图片路径...")
    fix_all_md_files(ceshi_path, images_dir)

    # 报告
    print("\n" + "=" * 50)
    print("同步完成！")
    print(f"🆕 新增笔记: {len(stats['new_md_files'])} 个")
    print(f"📝 更新笔记: {len(stats['updated_md_files'])} 个")
    for f in stats['updated_md_files'][:5]:
        print(f"   - {f}")
    if len(stats['updated_md_files']) > 5:
        print(f"   ... 还有 {len(stats['updated_md_files']) - 5} 个")

    print(f"\n✅ 新图片: {len(stats['new_images'])} 张")
    print(f"⏭️ 跳过已有: {len(stats['skipped_images'])} 张")

    if stats["not_found_images"]:
        print(f"\n❌ 未找到的图片 ({len(stats['not_found_images'])} 个):")
        for name in stats["not_found_images"][:5]:
            print(f"   - {name}")

    print("=" * 50)
    print("下一步：GitHub Desktop → Commit → Push")


def fix_all_md_files(ceshi_path, images_dir):
    """修复所有 md 文件中的图片路径"""
    image_files = {f.name for f in images_dir.iterdir() if f.is_file()}

    for md_file in ceshi_path.glob("*.md"):
        if md_file.name in ["fix_images.py", "sync_from_obsidian.py"]:
            continue

        content = md_file.read_text(encoding='utf-8')
        original_content = content

        pattern = r'!\[\[([^|\]#\n]+?)(?:[|\]#][^\]]*)?\]\]'

        def replace_link(match):
            image_name = match.group(1).strip()
            clean_name = image_name.replace('%20', ' ')

            # 跳过 canvas
            if clean_name.endswith('.canvas'):
                return f'![{clean_name}](./images/{clean_name})'

            found_name = None
            if clean_name in image_files:
                found_name = clean_name
            elif clean_name + '.png' in image_files:
                found_name = clean_name + '.png'
            elif clean_name + '.jpg' in image_files:
                found_name = clean_name + '.jpg'

            if found_name:
                url_name = found_name.replace(' ', '%20')
                return f'![{found_name}](./images/{url_name})'
            else:
                url_name = clean_name.replace(' ', '%20')
                return f'![{clean_name}](./images/{url_name})'

        new_content = re.sub(pattern, replace_link, content)

        if new_content != original_content:
            md_file.write_text(new_content, encoding='utf-8')
            print(f"  修复: {md_file.name}")


if __name__ == "__main__":
    sync_from_obsidian()