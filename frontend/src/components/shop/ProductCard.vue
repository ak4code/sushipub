<template>
    <div class="uk-card uk-card-small uk-box-shadow-hover-medium uk-card-default pub-product-card">
        <div class="uk-card-media-top uk-cover-container uk-position-relative" style="min-height: 250px">
            <img v-if="product.image" :src="product.image" class="uk-align-center" :alt="product.name" uk-cover>
            <img v-else src="/static/noimage.png" class="uk-align-center" :alt="product.name" uk-cover>
            <div class="pub-product-ingridients uk-flex uk-flex-middle uk-flex-center uk-flex-wrap uk-flex-wrap-middle">
                <div v-for="ig in product.ingredient_list" :key="ig.id" class="pub-ig">
                    {{ig.name}}
                </div>
            </div>
        </div>
        <div class="uk-card-body uk-text-center uk-card-small">
            <div class="pub-product-name">{{product.name}}</div>
            <div class="uk-text-muted" style="min-height: 30px">
                <small>{{product.size}}</small>
            </div>
            <div class="uk-flex uk-grid-small uk-child-width-1-2 uk-flex-middle uk-grid-match uk-margin-auto-vertical"
                 uk-grid>
                <div class="uk-text-muted uk-text-center">
                    <span v-if="product.weight">{{product.weight}} гр.</span>
                </div>
                <div class="pub-product-price uk-text-center">
                    <span>{{product.price}} ₽</span>
                </div>
            </div>
            <div class="uk-flex uk-flex-center uk-flex-bottom">
                <div>
                    <a @click="cartButton" class="uk-button pub-product-btn">
                        В корзину
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        name: "product-card",
        props: ['product'],
        methods: {
            ...mapActions({
                addItemToCart: 'addItemToCart'
            }),
            cartButton () {
                let item = {
                    qty: 1,
                    product: this.product
                }
                this.addItemToCart(item)
            }
        }
    }
</script>

<style scoped>

</style>