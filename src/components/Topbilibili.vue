<template>
  <div id='app'>
      
  <dv-full-screen-container>
    <dv-border-box-9>
      <div class="flex">
        
      <Wordcloud/><TopRightCharts/>
      <dv-border-box-10><h3>全B站Top1播放量(2021/12/13)</h3>
      <Number/>
      
      <Number2/>
      
      </dv-border-box-10>
      </div>
      <!-- 轮播图 -->
      <!-- <dv-border-box-8> -->
        <div class="box-8">
        <!-- <h3 style='text-align="center"'>排行榜</h3> -->
    <RightCharts/>
    <!-- 轮播图123 -->
    <RightCharts1/>
    <RightCharts2/>
    <RightCharts3/> 
        </div>
    <!-- </dv-border-box-8> -->
    <div class="flex1">
      
      <Board/>
      <Introduction/>
  </div>
   

    </dv-border-box-9> 
    </dv-full-screen-container>
  </div>
</template>

<script>
import Board from './pic/board.vue'
// import fullScreenContainer from "./fullScreenContainer/fullScreenContainer.vue";
import RightCharts from './pic/rightCharts.vue'
import RightCharts1 from './pic/rightCharts1.vue'
import RightCharts2 from './pic/rightCharts2.vue'
import TopRightCharts from './pic/topRightCharts.vue'
import RightCharts3 from './pic/rightCharts3.vue'
import Number from './pic/number.vue'
import Number2 from './pic/number2.vue'
import Wordcloud from './pic/wordcloud.vue'
import Introduction from './pic/introduction.vue'
export default {
  name: 'TopBilibili',
  components: {
    Number,
    Board, RightCharts,
    TopRightCharts,
    RightCharts1,
    RightCharts2,
   RightCharts3,
   Wordcloud,
   Number2,
   Introduction,
    // fullScreenContainer,
    
    // Number,
  },

}
</script>
<style scoped>
#dv-full-screen-container{
background-image:url('../assets/bg.png');
z-index: -999;
  margin:0;
}
#app {

  color: #fff;}
.box-8{
    width: 35%!important;
    float:right;
    margin-right:30px;
    border:0;
    height: 500px;

  }
#dv-border-box-11 {
    background-size: 100% 100%;
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
  }
  RightCharts1{
    position: relative;
    z-index:9999;
  }
  .flex{
    display:flex;
    flex-direction:row;
    align-items: center;
    align-content: stretch;
    justify-content: space-between;
  }
  .dv-border-box-10{
    z-index:-1;
  }

.flex1{
  
  display:flex;
  flex-direction:row;
  align-items: flex-end;
  align-items: center;


}
.dv-border-box-10{
  width:35%!important;
    margin-right:30px;
    margin-top:10px;
    border:0;
}

</style>
