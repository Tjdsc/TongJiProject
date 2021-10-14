<template>
  <div>
    <!--智能电池解决方案模块-->
    <div class="module_solution_title all_w">
        <h2>智能电池解决方案</h2>
        <span class="divider_line">——</span>
        <p>不仅仅提供企业算法上的解决方案，我们也提供算法方案之后云端到应用的服务方案</p>
        <p>整个生态链体系有完整的闭环，及时妥善解决您的问题</p>
    </div>
    <div class="module_solution_content all_w">
        <div class="animate__animated animate__lightSpeedInRight">
            <img src="../assets/product1.jpg" alt="">
            <div class="content_description">
                <img src="../assets/real_time_upload.png" alt="">
                <h4>实时观测电池老化</h4>
                <p class="algorithm_introduction">任何电池模组可以通过检测设备进行观测</p>
                <p class="algorithm_introduction">让您轻松知晓电池老化状态</p>
                <a href="#">了解更多</a>
            </div>
        </div>
        <div class="animate__animated animate__lightSpeedInRight">
            <img src="../assets/product2.jpg" alt="">
            <div class="content_description">
                <img src="../assets/early_warning.png" alt="">
                <h4>容量“跳水”多级预警</h4>
                <p class="algorithm_introduction">可靠算法支持</p>
                <p class="algorithm_introduction">让电池梯次利用最大化</p>
                <a href="#">了解更多</a>
            </div>
        </div>
        <div class="animate__animated animate__lightSpeedInRight">
            <img src="../assets/product3.jpg" alt="">
            <div class="content_description">
                <img src="../assets/quick_charge.png" alt="">
                <h4>超级快充</h4>
                <p class="algorithm_introduction">每个电池模组都可以有“个性化”定制快充方案</p>
                <p class="algorithm_introduction">安全高效，节省时间</p>
                <a href="#">了解更多</a>

            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
/*首页产品模块-start*/
.module_solution_title, .news_total_title{
    margin-top: 80px;
    text-align: center;
}
.module_solution_title h2, .news_total_title h2{
    font-size: 30px;
}
span.divider_line{
    /*margin-top: -40px;*/
    color: var(--main_color);
    font-weight: bolder;
    font-size: 35px;
}
.module_solution_title p{
    color: #9c9c9c;
    font-size: 14px;
    line-height: 2em;
}
.module_solution_content{
    margin-top: 20px;
}
.module_solution_content div{
    overflow: hidden;
    position: relative;
    margin: 30px 0;
    width: 100%;
    height: 600px;
}
/*背景动画*/
@keyframes kenburns-top-right {
    0% {
        transform: scale(1) translate(0, 0);
        transform-origin: 84% 16%;
    }
    100% {
        transform: scale(1.25) translate(20px, -15px);
        transform-origin: right top;
    }
}
.module_solution_content div img{
    width: 100%;
    height: 100%;
    animation: kenburns-top-right 5s ease-out both;
}
.module_solution_content div .content_description{
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 450px;
    height: 360px;
    background-color: rgba(0,0,0,.2);
    text-align: center;
}
.module_solution_content div .content_description img{
    margin-top: 50px;
    width: 45px;
    height: 40px;
    animation: none;
}
.content_description h4,.algorithm_introduction,a{
    color: var(--slideshow-text-color);
}
.content_description h4{
    margin: 30px 0 20px 0;
    font-size: 20px;
    font-weight: normal;
}
.content_description p{
    line-height: 2em;
    font-size: 14px;
}
.content_description a{
    margin-top: 35px;
    display: inline-block;
    width: 80px;
    height: 40px;
    border-bottom: 1px solid var(--main_color) ;
    font-size: 16px;
    transition: all .6s;
}
.content_description a:hover{
    transform: translateY(-10px);
}
/*首页产品模块-end*/
</style>