<template>
    <div class="uk-card uk-card-small uk-box-shadow-hover-medium uk-card-default pub-product-card">
        <div class="uk-card-media-top uk-cover-container uk-position-relative" style="min-height: 250px">
            <img v-if="checkedProduct.image || product.image" :src="checkedProduct.image || product.image" class="uk-align-center" :alt="checkedProduct.name" uk-cover>
            <img v-else src="/static/noimage.png" class="uk-align-center" :alt="checkedProduct.name" uk-cover>
            <div class="pub-product-ingridients uk-flex uk-flex-middle uk-flex-center uk-flex-wrap uk-flex-wrap-middle">
                <div v-for="ig in product.ingredient_list" :key="ig.id" class="pub-ig">
                    {{ig.name}}
                </div>
            </div>
        </div>
        <div class="uk-card-body uk-text-center uk-card-small">
            <div class="pub-product-name">{{product.name}}</div>
            <div class="product-size uk-margin-small" style="min-height: 30px">
                <div class="uk-text-muted" v-if="!product.variants.length">
                    <small>{{product.size}}</small>
                </div>
                <div v-else>
                    <el-radio-group v-model="selectedProduct" @change="changeProduct" size="mini">
                        <el-radio-button :label="product.id">{{product.size}}
                        </el-radio-button>
                        <el-radio-button v-for="variant in product.variants"
                                         :key="variant.id"
                                         :label="variant.id"
                        >{{variant.size}}
                        </el-radio-button>
                    </el-radio-group>
                </div>
            </div>
            <div class="uk-flex uk-grid-small uk-child-width-1-2 uk-flex-middle uk-grid-match uk-margin-auto-vertical"
                 uk-grid>
                <div class="uk-text-muted uk-text-center">
                    <span v-if="checkedProduct.weight">{{checkedProduct.weight}} гр.</span>
                </div>
                <div class="pub-product-price uk-text-center">
                    <span>{{checkedProduct.price}} ₽</span>
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
        data: () => ({
            selectedProduct: null,
            checkedProduct: {
                id: null,
                name: null,
                image: null,
                price: null,
                size: null,
            }
        }),
        mounted () {
            this.selectedProduct = this.product.id
            this.checkedProduct = this.product
        },
        methods: {
            ...mapActions({
                addItemToCart: 'addItemToCart'
            }),
            cartButton () {
                let item = {
                    qty: 1,
                    product: this.checkedProduct
                }
                this.addItemToCart(item)
            },
            changeProduct (id) {
                let variant = this.product.variants.find(v => v.id === id)
                if (variant) {
                    this.checkedProduct = variant
                } else {
                    this.checkedProduct = this.product
                }
            }
        }
    }
</script>

<style scoped>

</style>