# -*- coding: utf-8 -*-  
import os
import json

OUTPUT_FILE_PATH = "tv_new.json"; # 最后的结果文件
INPUT_FILE_PATH = "all.txt"; # 原始的，需要解析的文件 


def parse_new_data():
    lines = open(INPUT_FILE_PATH, "r", encoding='utf-8').readlines();
    data_set = set();
    output_file = open(OUTPUT_FILE_PATH, "w", encoding="utf-8")
    output_file.write('{\n\t\"dict":[\n\t\t')
    for i in range(1, len(lines)):
        try:
            column = lines[i].strip().split();
            mtype = column[1];
            title = column[2];
            tt = title.strip().split('/');
            #print(type(tt[1]));
            for k in range(0, len(tt)):
                data_set.add(tt[k]);
            #print(data_set);
            json_result = {"dict":[{"majorType":"tv", "minorType":"", "value":[]}]};
            dictionary = json_result["dict"][0];
            dictionary["minorType"] = mtype;
            dictionary["value"] = list(data_set);
            json.dump(dictionary, output_file, indent=4,  ensure_ascii=False)
            output_file.write(',\n')
            data_set.clear()
        except:
            print("errrrrrrrrrrrrror!");
    return data_set;

def main():
    parse_new_data();

main();

