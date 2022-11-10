<template>
  <el-container class="container">
    <h1>Discover author interaction in the future</h1>
    <p>Search our AI curated corpus of 2000 author, 8000 publication belong to those authors and 100,000 interactions and explore the related research. This site is a free service of the non-profit for AI.</p>
    <div class="box-notice">
      <strong>Extra information :</strong>
      <span class="read-normal"> The information contained herein should NOT be used as a substitute for the advice of an appropriately qualified and licensed physician or other health care provider. The tool is not a substitute for the care provided </span>
      <span class="read-more">by licensed healthcare practitioners and consumers are urged to consult with their healthcare practitioner in all instances. The absence of a warning for a given supplement, drug or combination thereof in no way should be construed to indicate that the supplement, drug or combination is safe, effective or appropriate for any given patient. The information provided here is for informational purposes only. This tool may not cover all possible supplement-drug interactions. Please check with a physician if you have health questions or concerns. Although we attempt to provide accurate and up-to-date information, no guarantee is made to that effect. This tool does not endorse any drugs or supplements, diagnose patients, or recommend therapy.</span>
    </div>
    <el-button type="text" class="read-more-btn">{{textBtnMoreLess}}</el-button>
    <SreachBox></SreachBox>
    <AboutSection></AboutSection>
    <TeamSection></TeamSection>
  </el-container>
</template>

<script>
import SearchBox from './components/SearchBox.vue';
import TeamSection from './components/TeamSection.vue';
import AboutSection from './components/AboutSection.vue';
export default {
components: {
  SreachBox : SearchBox,
  AboutSection: AboutSection,
  TeamSection: TeamSection,
},
data(){
  return{
    isMore: false,
    textBtnMoreLess: "Show more"
  }
},
methods: {
  ShowLessMore(){
    this.isMore = !this.isMore
    if(this.isMore === true){
      this.textBtnMoreLess = "Show less"
    }
    else{
      this.textBtnMoreLess = "Show more"
    }
  }
},
}
</script>

<style lang="scss" scoped>
.el-container{
    display: inline-block;
    width: 900px;
    margin: 10%;
    margin-top: 0px;
    margin-bottom: 0px;
    padding : 1.5rem;
    padding-left: 0px;
    padding-right: 0px;
    h1 {
        font-family: Raleway,Helvetica Neue,Helvetica,-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
        font-variant-numeric: lining-nums;
        font-weight: 700;
        font-size: 2.25rem;
        line-height: 2.5rem;
    }
    .box-notice{
        box-sizing: border-box;
        width: 100%;
        border: 1px solid rgb(166, 222, 246);
        background: rgb(241, 250, 255);
        padding : 1rem;
        color: #4c5258;
        border-radius: 4px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
}
#read-more {
  display: none;
}

</style>