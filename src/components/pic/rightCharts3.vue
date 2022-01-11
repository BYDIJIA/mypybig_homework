<template>
  <div id="right_chart3">
    <h4>运动Top100-评论量</h4>
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
        this.getsportscomm();
      });
    },
    methods:{
      async getsportscomm(){
        await this.axios
        .get('/get_sports_comm')
        .then((res)=>{
            this.config={
              data:res.data,
              rowNum:1,
               align:['center'],
              headerHeight:10,
              index:true,

           }
              //  console.log(res.data) 
        })
        this.config={...this.config}
     
      },
    },

};
</script>

<style>

</style>