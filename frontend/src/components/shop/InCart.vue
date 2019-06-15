<template>
    <div class="uk-flex uk-flex-center uk-flex-bottom">
        <div>
            <a @click="cartButton" class="uk-button pub-product-btn">
                В корзину
            </a>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        name: "in-cart",
        props: ['productId'],
        data: () => ({
            product: {}
        }),
        created () {
            this.getProduct(this.productId)
        },
        methods: {
            ...mapActions({
                addItemToCart: 'addItemToCart'
            }),
            async getProduct (id) {
                let {data} = await this.$axios.get(`/api/products/${id}`)
                this.product = data
            },
            cartButton () {
                let item = {
                    qty: 1,
                    product: this.product
                };
                this.addItemToCart(item)
                this.$notify.success('Добавлено в корзину')
            }
        }
    }
</script>

<style scoped>

</style>