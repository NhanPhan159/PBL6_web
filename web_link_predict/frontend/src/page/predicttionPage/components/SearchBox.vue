<template>
  <el-card class="card">
    <div slot="header">
        <h1> Search</h1>
    </div>
    <div>
        <el-input placeholder="Enter name of the author" v-model="search_name"></el-input>
        <el-row type="flex">
            <el-col :span="20"><span>Try : </span></el-col>
            <el-col :span="4"><span>Last update : {{last_update}}</span></el-col>
        </el-row>
    </div>
  </el-card>
</template>

<script>
export default {
    data(){
        return{
            search_name : null,
            last_update: "2022"
        }
    }
}
</script>

<style lang="scss" scoped>
.card{
     font-weight: 700;
     .el-input {
        margin-bottom: 1rem;
     }
     h1 {
        font-size: 1.875rem;
        line-height: 2.25rem;
        margin: 0px;
     }
}

</style>