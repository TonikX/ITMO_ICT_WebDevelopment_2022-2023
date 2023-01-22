<template>
    <div class="container" id="telo" style="padding-top: 100px">
        <div class="row">
            <div class="col-md-6">
                <div style="display: flex">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="HeroPill__NakedBitcoinIcon-sc-16ndsef-1 epDkoW"><path d="M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12z" fill="#1652F0"></path><path d="M17.274 10.515c.235-1.572-.962-2.417-2.599-2.981l.531-2.13-1.296-.323-.517 2.074c-.34-.086-.69-.165-1.039-.245l.521-2.087L11.58 4.5l-.53 2.13c-.283-.065-.56-.128-.829-.196l.002-.007-1.788-.446-.345 1.385s.962.22.942.234c.525.13.62.478.603.754L9.03 10.78c.036.01.083.023.135.043l-.137-.034-.848 3.4c-.064.158-.227.398-.595.307.014.019-.941-.235-.941-.235L6 15.745l1.688.42c.313.08.62.162.923.239l-.537 2.154 1.296.322.53-2.13c.355.096.698.184 1.034.268l-.53 2.121 1.297.323.536-2.15c2.211.419 3.873.25 4.573-1.75.564-1.61-.028-2.538-1.191-3.144.847-.195 1.485-.752 1.655-1.903zm-2.963 4.153c-.4 1.61-3.11.74-3.99.522l.713-2.854c.879.22 3.697.654 3.277 2.332zm.402-4.176c-.365 1.464-2.621.72-3.353.537l.645-2.587c.731.182 3.089.522 2.708 2.05z" fill="#fff"></path></svg>
                    <a href="/register" style="display: flex">&nbsp&nbspНачните формировать свой портфель</a>
                </div>
                <div>
                    <h1 class="title_h1_main_page">
                        Начните<br>формировать<br>свой<br>криптовалютный<br>портфель
                    </h1>
                    <h4 class="description_after_h1_main_page">
                        Coinbase — самая удобная площадка для купли и продажи криптовалюты. Зарегистрируйтесь и начните прямо сегодня.
                    </h4>
                </div>
            </div>

            <div class="col-md-6">
                <img src="../assets/img/main_page-f1a95755.png" height="534px" width="526px">
            </div>
        </div>
    </div>
</template>




<script>
export default {
    name: "bodyBlock"
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
:root{
    --back-color: #000000;
    --login-in-system: #ffffff;
    --telo-background-color: #000000;
    --bodykit--background-color: #000000;
    --title-h1-main-page: #ffffff;
    --description-after-h1-main-page: #ffffff;


}
</style>
