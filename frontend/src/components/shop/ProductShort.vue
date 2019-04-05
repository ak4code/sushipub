<template>
    <div class="uk-flex uk-grid-small uk-grid-match uk-margin-small-bottom uk-child-width-1-1 uk-child-width-1-5@m"
         uk-grid v-if="products.length">
        <div v-for="product in products" :key="product.id">
            <product-card :product="product"></product-card>
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
    import ProductCard from '@/components/shop/ProductCard'
    export default {
        name: "product-list",
        props: {
            categoryId: {
                type: Number,
                required: true
            }
        },
        components: {
            ProductCard
        },
        data: () => ({
            products: [],
            category: null,
            count: 0
        }),
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products/short_list?category=${this.categoryId}`)
                this.products = data
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