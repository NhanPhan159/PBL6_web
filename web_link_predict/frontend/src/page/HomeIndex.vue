<template>
  <div>
    <div class="nav-container">
        <nav class="menu">
            <div class="logo">
                
            </div>
            <ul class="navbar">
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/AddData">Add</router-link></li>
            </ul>
        </nav>
    </div>
    <router-view/>
    <el-footer class="footer">
        <center><p>DUT non-profit private project </p></center>
    </el-footer>

  </div>
</template>

<script>
export default {
    components: {
    }
}
</script>

<style lang="scss">
img {
    height: 56px;
    width: 56px;
}
.footer{
    background: rgb(249, 250, 250);
}
.nav-container {
        position: sticky;
        top: 0;
        width: 100%;
        background-color:   #f3e2b3 ;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
    }

    nav.menu {
        display: flex;
    }

    ul {
        list-style-type: none;

    }

    ul.navbar li {
        display: inline;
    }

    .main-container {
        height: 1200px;
    }

    .logo,
    .navbar {
        margin: 15px auto;
        padding: 0;

    }

    nav a {
        text-decoration: none;
        color: #112e51;
    }

    ul.navbar {
        display: flex;
    }

    ul.navbar>li a {
        padding: 8px;
        border: 1px solid transparent;
        background: inherit;
        border-radius: 8px;

    }

    ul.navbar>li a:hover {
        padding: 8px;
        border: 1px solid black;
        border-radius: 8px;


    }

    @media screen and (max-width: 600px) {
        nav.menu {
            flex-wrap: wrap;
            text-align: center;
        }

        .logo,
        .navbar {
            flex: 100%;
        }

        ul.navbar {
            justify-content: center;
        }


    }
p {
    font-family: Lato, "Helvetica Neue", Helvetica, -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 1rem;
    line-height: 1.375rem;
    color: #4c5258;
    margin-bottom: 1px;

}
</style>