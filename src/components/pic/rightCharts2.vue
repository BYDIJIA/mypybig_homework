<template>
  <div id="right_chart2">
    <h4>食物Top100-播放量</h4>
      <dv-scroll-board :config="config" style="width: 500px; height: 50px" />
  </div>
</template>

<script>
export default {
    data() {
        
        return{
            config:{
        },
    };
    },
    created() {
      this.$nextTick(()=>{
        this.getfoodplay();
      });
    },
    methods:{
      async getfoodplay(){
        await this.axios
        .get('/get_food_play')
        .then((res)=>{
            this.config={
              data:res.data,
              rowNum:1,
               align:['center'],
              headerHeight:10,
              index:true, 
          
          }
          // console.log(res.data)
        })
        this.config={...this.config}
         
      },
    },

};
</script>

<style>
#right_chart2{
  position: relative;
  z-index:999;
}
</style>