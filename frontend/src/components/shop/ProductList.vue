<template>
    <div class="uk-flex uk-grid-small uk-grid-match uk-margin-small-bottom uk-child-width-1-1 uk-child-width-1-5@m"
         uk-grid v-if="products.length">
        <div v-for="product in products" :key="product.id">
            <div class="uk-card uk-card-small uk-card-default pub-product-card">
                <div class="uk-card-media-top">
                    <img :src="product.image" :alt="product.name">
                </div>
                <div class="uk-card-body uk-text-center uk-padding-remove">
                    <span class="pub-product-name">{{product.name}}</span>
                    <br>
                    <small class="uk-text-muted">{{product.quantity}} шт.</small>
                    <div class="uk-flex uk-grid-small uk-child-width-1-2 uk-flex-middle uk-grid-match uk-margin-auto-vertical"
                         uk-grid>
                        <div class="uk-text-muted uk-text-center">
                            <span>{{product.weight}} гр.</span>
                        </div>
                        <div class="pub-product-price uk-text-center">
                            <span>{{product.price}} ₽</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="category">
            <a :href="category.link" class="uk-flex uk-flex-middle uk-text-large uk-text-center pub-product-cat-link">
                <div class="uk-width-1-1">
                    Показать все
                    <br>
                    {{category.name}}
                </div>
            </a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "product-list",
        props: {
            limit: {
                type: Number,
                default: 30
            },
            categoryId: {
                type: Number,
                required: true
            }
        },
        data: () => ({
            products: [],
            category: null,
            count: 0,
            next: null,
            previous: null,
        }),
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products?category=${this.categoryId}&page_size=${this.limit}`)
                this.products = data.results
                this.count = data.count
                this.next = data.next
                this.previous = data.previous
                await this.getCategory()
            },
            async getCategory () {
                let {data} = await this.$axios.get(`/api/categories/${this.categoryId}`)
                this.category = data
            }
        }
    }
</script>

<style scoped>

</style>