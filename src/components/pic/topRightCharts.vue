<template>
  <div id="topRightCharts">
    <!-- 胶囊图 -->
    <!-- <dv-border-box-8> -->
      <h3>每排行榜的Top1up主的评论量</h3>
      <dv-capsule-chart :config="config" style="width:300px;height:200px" />
      <!-- </dv-border-box-8> -->
  </div>
</template>

<script>
export default {
    data() {
        
        return{
            config:{
             data: [
  {
    "name": "原神",
    "value": "1.6"
  },
  {
    "name": "大漠叔叔",
    "value": "1.8"
  },
  {
    "name": "腾讯音乐娱乐集团",
    "value": "2.6"
  },
  {
    "name": "燕子堡BBQ学徒Ray",
    "value": "5"
  },
  {
    "name": "啊吗粽",
    "value": "2.4"
  },
  
],
unit:'万',
showValue:true,
        },
    };
    },

};
</script>

<style scoped>
#topRightCharts{
  display: flex;
  flex-direction:column-reverse;
  z-index: 999;
}
.dv-border-box-8{
  /* width: 50%!important; */
  padding-right:40px;
  padding-top:30px;
  padding-left: 30px;
  padding-bottom:50px;
 margin-top:150px;
 align-items: flex-end;
 justify-content:flex-end;
}
h3{
  text-align: center!important;
}
</style>