<template>
  <div
      style="height:560px; background-color: #FFFFFF; overflow:hidden; box-sizing: border-box; border: 1px solid rgb(94, 94, 94); border-radius: 4px; text-align: right; line-height:14px; font-size: 12px; font-feature-settings: normal; box-shadow: inset 0 -20px 0 0 rgb(94, 94, 94); padding:1px; margin: 0; width: 100%;">
    <div style="height:540px; padding:0; margin:0; width: 100%;" id="currency">
      <iframe
          :src="`https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=${currency_coinlib_id}&pref_coin_id=1505`"
          width="100%"
          height="536px" border="0" style="border:0; margin:0; padding:0; line-height:14px;"></iframe>
    </div>
    <div
        style="color: #FFFFFF; line-height: 14px; font-weight: 400; font-size: 11px; box-sizing: border-box; padding: 2px 6px; width: 100%; font-family: Verdana, Tahoma, Arial, sans-serif;">
      <a href="https://coinlib.io" target="_blank"
         style="font-weight: 500; color: #FFFFFF; text-decoration:none; font-size:11px">
        Cryptocurrency Prices
      </a>&nbsp;by Coinlib
    </div>
  </div>
</template>

<script>
export default {
  name: "CurrencyChart",
  props: {
    currency_coinlib_id: 859
  }
}
</script>
