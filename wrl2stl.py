import bpy
import os
import sys

def get_files_with_extension(folder_path, extension):
    file_names = []
    for file in os.listdir(folder_path):
        if file.endswith(extension):
            file_names.append(file)
    return file_names

def convert_wrl_to_stl(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".wrl"):
            # 既存のBlenderシーンをクリア
            bpy.ops.wm.read_factory_settings(use_empty=True)

            # WRLファイルをインポート
            input_file = os.path.join(input_folder, file)
            bpy.ops.import_scene.x3d(filepath=input_file)

            # STLファイルとしてエクスポート
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".stl")
            bpy.ops.export_mesh.stl(filepath=output_file, use_selection=True)

            # オブジェクトを削除
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()

            # 全シーンオブジェクトを削除する
            for item in bpy.context.scene.objects:
                bpy.context.scene.objects.unlink(item)

            print(f"Converted {file} to STL.")

    print("Conversion completed.")

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Usage: blender --background --python wrl2stl.py -- <input_folder> <output_folder>")
        sys.exit(1)
    else:
        # 変換元のwrlファイルパス
        input_folder = sys.argv[5]
        print(input_folder)
    
        # 出力するSTLファイルのパス
        output_folder = sys.argv[6]
        print(output_folder)

    # 変換元の拡張子として".wrl"を指定
    input_extension = ".wrl"
    
    # 変換元のフォルダ内のWRLファイル名を取得
    input_file_names = get_files_with_extension(input_folder, input_extension)

    # WRLからSTLへ変換
    convert_wrl_to_stl(input_folder, output_folder)
