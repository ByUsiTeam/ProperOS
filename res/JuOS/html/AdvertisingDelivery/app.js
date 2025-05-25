//import config from "./config.js";

// url("./src/item-0.png")

let config = {
    'r': '30px',    // 圆角
    'bg': 'white',  // 背景
    'y': '10px',    //上下边距
    'x': '10px',    // 左右边距
    'index': 0,     // 初始化第几张展开
    'time': 1000,   // 轮播时间单位毫秒
    'play': true,   // 是否播放
    // 图片路径 支持网络图片部分格式不支持
    'imgPath': [
        './src/aimg_01.png',
        './src/aimg_02.png',
        './src/aimg_03.png',
        './src/aimg_04.png',
        './src/aimg_14.png',
        './src/aimg_07.png',
    ]
}

window.onload = function () {
    // 初始化
    (function () {
        document.body.style.setProperty("--r", config.r)
        document.body.style.setProperty("--bg", config.bg)
        document.body.style.setProperty("--x", config.x)
        document.body.style.setProperty("--y", config.y)

    })()
    let index = config.index
    const ul = document.querySelector('.container>ul');
    ul.addEventListener('click', function (e) {
        const element = e.target
        if (element.tagName === 'IMG' || element.tagName === 'LI') {

            for (let i = 0; i < ul.childElementCount; i++) {
                ul.children[i].className = ''
            }
            element.parentElement.className = 'active'
        }
    })
    render(config.imgPath)

    if (config.play) {
        setInterval(() => {
            if (index < ul.childElementCount - 1) {
                index++;
            } else {
                index = 0
            }
            for (let child of ul.children) {
                child.className = ''
            }
            ul.children[index].className = 'active'

        }, config.time)
    }


    function render(paths = []) {
        let str = ''
        for (let i = 0; i < paths.length; i++) {

            if (i === config.index) {
                str += `
                <li class="active">
                    <img alt="" src="${paths[i]}">
                </li>
            `
            } else {
                str += `
                <li>
                    <img alt="" src="${paths[i]}">
                </li>
            `
            }

        }
        ul.innerHTML = str
    }
}