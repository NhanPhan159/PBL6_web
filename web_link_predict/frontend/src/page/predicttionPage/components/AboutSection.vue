<template>
  <div class="about-container">
    <h1>About</h1>
    <p>The development and expansion of science has led to an increase in the number of scientists, which means more and more scientific articles. Including many co-authored articles. The question is whether we can predict the future collaboration of researchers or authors to recommend suitable co-author candidates.</p>
    <p>
To solve this problem, the research team used topic modeling to classify the authors, thereby building a graph of the association between the authors</p>
    <p>To find out more about this work, please read our <a href="#">publication</a>.</p>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.about-container{
    color: #4c5258;
    width: 100% !important;
    box-sizing: border-box;
    font-family: Raleway,Helvetica Neue,Helvetica,-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;
}
h1{
    font-size: 1.875rem;
    line-height: 2.25rem;
}
p{
    margin-bottom: 1.5rem;
}
</style>