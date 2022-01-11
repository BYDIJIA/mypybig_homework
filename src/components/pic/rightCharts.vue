<template>
  <div id="right_chart">
    <h4>知识Top100-评论量</h4>
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
        this.getknowledgecomm();
      });
    },
    methods:{
      async getknowledgecomm(){
        await this.axios
        .get('/get_knowledge_comm')
        .then((res)=>{
            this.config={
              // header:['title','commit'],
              data:res.data,
              rowNum:1,
              headerHeight:10,
              align:['center'],
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

</style>