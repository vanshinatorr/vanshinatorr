import sys

def main():
    try:
        with open('temp_streak.svg', 'r') as f:
            content = f.read()

        # 1. Update viewBox and dimensions
        content = content.replace(
            "viewBox='0 0 495 195' width='495px' height='195px'",
            "viewBox='0 0 495 220' width='495px' height='220px'"
        )

        # 2. Update clipPath rect
        content = content.replace(
            "<rect width='495' height='195' rx='4.5'/>",
            "<rect width='495' height='220' rx='4.5'/>"
        )

        # 3. Update inner border rect height
        content = content.replace(
            "width='494' height='194'",
            "width='494' height='219'"
        )

        # 4. Update the second isolation group to translate the graphics down
        target_str = "</g>\n            <g style='isolation: isolate'>\n                <line x1='165'"
        replacement_str = "</g>\n            <g style='isolation: isolate' transform='translate(0, 12.5)'>\n                <line x1='165'"
        content = content.replace(target_str, replacement_str)

        # 5. Append root border rect before closing svg tag
        svg_close_target = "</g>\n    </svg>"
        svg_close_replacement = "</g>\n    <rect x=\"0.5\" y=\"0.5\" width=\"494\" height=\"219\" fill=\"none\" stroke=\"#1e293b\" stroke-width=\"1\" rx=\"4.5\" ry=\"4.5\" />\n</svg>"
        content = content.replace(svg_close_target, svg_close_replacement)

        with open('temp_streak.svg', 'w') as f:
            f.write(content)

        print("Streak stats SVG post-processed successfully for height=220px.")
    except Exception as e:
        print(f"Error during post-processing: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
