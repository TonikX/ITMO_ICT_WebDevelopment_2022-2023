<template>
    <nav class="navbar navbar-expand-lg navbar-light" id="shapka">
        <div class="container-fluid" style="padding-right: 40px;padding-left: 40px;">
            <div class="navbar-header">
                <a href="Main.html"><img src="https://images.ctfassets.net/q5ulk4bp65r7/3TBS4oVkD1ghowTqVQJlqj/2dfd4ea3b623a7c0d8deb2ff445dee9e/Consumer_Wordmark.svg" height="20" width="112" alt="Логотип Coinbase"></a>
            </div>
            <div>
                <ul class="nav navbar-nav">
                    <a href="/Login" class="pull-right loginIn">Войти в систему</a>
                    <a class="iksweb" href="/Register" title="Начать">Начать</a>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "headerBlock"
}
</script>
<style scoped>
.loginIn{

  font-family: 'NotoSansDisplay', sans-serif;
  font-size: 14px;
  font-weight: bold;
  color: var(--login-in-system);
}
.loginIn:hover{
  color:#0051ff;

}
/* Стили кнопки */
.iksweb
{
  display: inline-block;
  cursor: pointer;
  font-size: 13px;
  text-decoration:none;
  padding:10px 20px;
  color:#ffffff;
  background:#0051ff;
  border-radius:5px;
  border:2px solid #0052ff;
}
.iksweb:hover{
  display: inline-block;
  cursor: pointer;
  font-size: 13px;
  text-decoration:none;
  padding:10px 20px;
  color:#ffffff;
  background: #063498;
  border-radius:5px;
  border:2px solid #0052ff;
}
.navbar.navbar-expand-lg.navbar-light.bg-light{
  background-color: var(--back-color);
}
.loginIn{
  margin-right: 10px;
  color: var(--login-in-system);
  display: flex;
  align-items: center;
}
#shapka{
  background-color: var(--back-color);
}
#telo{
  background-color: var(--telo-background-color);
}
#bodykit{
  background-color: var(--bodykit--background-color);
}
.title_h1_main_page{
  color: var(--title-h1-main-page);
}
.description_after_h1_main_page{
  color: var(--description-after-h1-main-page)
}

</style>











