<template>
    <div class="pub-cart-button">
        <div class="pub-cart-counter">{{items.length}}</div>
        <img src="/static/src/assets/img/cart.svg" width="30" height="30" style="color: #bf0909;"
             uk-svg>
        <div class="pub-cart-total" v-if="total">{{total}}р.</div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        name: "cart-button",
        data: () => ({}),
        created () {
            this.getCart()
        },
        mounted () {

        },
        watch: {
            total: function () {
                UIkit.toggle(document.querySelector('.pub-cart-button'), {
                    animation: 'uk-animation-scale-up',
                    cls: 'sd'
                }).toggle()
            }
        },
        computed: {
            ...mapGetters({
                items: 'getItems',
                total: 'getTotal'
            })
        },
        methods: {
            ...mapActions({
                getCart: 'getCartItems'
            })
        }
    }
</script>

<style scoped>

</style>