"""
Stretches animation frame pngs to fit a larger animation rate.
http://github.com/redoverture
https://osu.ppy.sh/users/3959060
"""
__author__ = "redoverture"
__license__ = "MIT License"
import shutil
import pathlib

# Change Below to Use!
###########################################
skin_folder = pathlib.Path("path/to/skin")
output_folder = pathlib.Path("output")
file_prefix = "followpoint"
animation_rate = 60
###########################################


def main():
    print("== osu! Asset Stretcher v1.0 ==")
    print(f"Animation Rate: {animation_rate}")
    print(f"Skin/Input Folder: {skin_folder}")
    print(f"Asset Output Folder: {output_folder}")
    print(f"Target Animation Rate: {animation_rate}")
    print(f"Matching prefix: '{file_prefix}")
    print("====================================")

    output_folder.mkdir(exist_ok=True)

    frames = list(skin_folder.glob(f"{file_prefix}*.png"))
    scale_factor = animation_rate // len(frames)
    rem = animation_rate - (scale_factor * len(frames))

    print(f"Found {len(frames)} frames of animation.")
    print(f"Duplicating each frame {scale_factor} times.")
    if rem > 0:
        print(f"Last frame will be duplicated {rem} times to fit evenly into {animation_rate}.")

    for idx, frame in enumerate(frames):
        base = idx * scale_factor
        for i in range(0, scale_factor):
            shutil.copy(frame, output_folder/f"{file_prefix}-{base + i}.png")
        if idx == len(frames) - 1:
            for i in range((animation_rate - rem), animation_rate):
                shutil.copy(frame, output_folder/f"{file_prefix}-{i}.png")

    print(f"Done. Check {output_folder.resolve()} for your shiny, stretched assets!")


if __name__ == "__main__":
    main()
