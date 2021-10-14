<template>
<!--轮播图模块-->
<div class="slideshow">
    <ul class="slides">
        <input type="radio" id="control-1" name="control" checked>
        <input type="radio" id="control-2" name="control">
        <input type="radio" id="control-3" name="control">

        <li class="slide">
            <img src="../assets/advertising1_1.jpg" alt="">
            <div class="introduction1 animate__animated animate__fadeInBottomLeft">
                <h3>实时观测电池老化状态</h3>
                <h4>多种算法支持 实时更新 提前预警</h4>
                <a href="#">了解详情</a>
            </div>
        </li>
        <li class="slide">
            <img src="../assets/advertising2.jpg" alt="">
            <div class="introduction2">
                <h3>把握电池梯次利用的“转折点”</h3>
                <h4>多级预警 精确预测</h4>
                <a href="#">了解详情</a>
            </div>
        </li>
        <li class="slide">
            <img src="../assets/advertising3.jpg" alt="">
        </li>
        <div class="controls-visible">
            <label for="control-1"></label>
            <label for="control-2"></label>
            <label for="control-3"></label>
        </div>
    </ul>
</div>
</template>

<script>
export default {

}
</script>

<style>
/*轮播图模块-start*/
ul.slides{
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 700px;
}
li.slide{
    /*float: left;*/
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all .5s;
}
ul li.slide img{
    width: 100%;
    height: 100%;
}
.slide:nth-of-type(2){
    left: 100%;
}
.slide:nth-of-type(3){
    left: 200%;
}
input[type="radio"]{
    position: relative;
    z-index: 100;
    display: none;
}
.controls-visible{
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 12px;
}
.controls-visible label{
    display: inline-block;
    height: 16px;
    width: 16px;
    background-color: #fff;
    border-radius: 50%;
    margin: 0 8px;
    border: 2px solid #ffffff;
}
/*首先加入.slides input[type="radio"]:nth-of-type(1):checked判断当第一个radio按钮是已选择的状态时，加入~符号，找它同一层之后，
.controls-visible里面的label:nth-of-type(1)，选择到第一个label*/
.slides input[type="radio"]:nth-of-type(1):checked~.controls-visible label:nth-of-type(1){
    background-color: #333;
}
.slides input[type="radio"]:nth-of-type(2):checked~.controls-visible label:nth-of-type(2){
    background-color: #333;
}
.slides input[type="radio"]:nth-of-type(3):checked~.controls-visible label:nth-of-type(3){
    background-color: #333;
}
/*当选中了第一个radio按钮之后，后面三张.slide的样式*/
.slides input[type="radio"]:nth-of-type(1):checked~.slide{
    transform: translateX(0%);
}
.slides input[type="radio"]:nth-of-type(2):checked~.slide{
    transform: translateX(-100%);
}
.slides input[type="radio"]:nth-of-type(3):checked~.slide{
    transform: translateX(-200%);
}
/*第一张图文字*/
ul li.slide .introduction1{
    position: absolute;
    left: 15%;
    top: 30%;
}
ul li.slide h3{
    color: var(--slideshow-text-color);
    font-size: 60px;
}
ul li.slide h4{
    color: var(--slideshow-text-color);
    font-size: 30px;
    font-weight: normal;
    padding-top: 15px;
    text-align: center;
}
ul li.slide a{
    display: inline-block;
    width: 150px;
    height: 50px;
    margin: 60px 160px;
    font-size: 16px;
    color: var(--slideshow-text-color);
    border: 1px solid var(--slideshow-text-color);
    text-align: center;
    line-height: 50px;
}
/*第二张图文字*/
ul li.slide .introduction2{
    position: absolute;
    width: 900px;
    left: 50%;
    top: 20%;
    transform: translateX(-50%);
    background-color: rgba(0,0,0,.3);
    text-align: center;
    padding: 20px;
    border-radius: 10px;
}
/*轮播图模块-end*/
</style>