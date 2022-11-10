<template>
  <div>
    <el-card>
      <div class="title">
        <h1>New data</h1>
        <p>
          This site is use for loading new data to database so please make all
          the information in data is valid, this can make the prediction more
          clearly
        </p>
      </div>
    </el-card>
    <el-row type="flex" justify="end">
      <el-col :span="2"
        ><el-button type="primary" plain class="btn-add" @click="print()"
          >Add data</el-button
        ></el-col
      >
    </el-row>
    <el-upload
      class="upload"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      :on-change="handelTotal"
      :multiple="false"
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <div class="el-upload__tip" slot="tip">
        jpg/png files with a size less than 500kb
      </div>
    </el-upload>
    {{data.length}}
  </div>
</template>

<script>
import papaparse from "papaparse";
export default {
  data() {
    return {
      tableAuthor: [],
      header: [],
    };
  },
  methods: {
    assignData(data){
      for(let i = 0;  i< data.length;i++)
        {
          let obj = {
            'col1' : data[i][3]
          }
          this.tableAuthor.push(obj)
        }
      console.log(this.tableAuthor)
    },
    handleImport(file, callBack) {
      papaparse.parse(file.raw, {
        download: true,
        dynamicTyping: true,
        complete: function(results){
          callBack(results.data)
        },
      })
    },
    handelTotal(file){
      this.handleImport(file, this.assignData)
    },
    

  },
  computed:{
    data(){return this.tableAuthor}
  }
};
</script>

<style lang="scss" scoped>
.title {
  text-align: center;
}
.btn-add {
  margin: 1rem;
}
.upload {
  margin: auto;
  display: table;
}
</style>