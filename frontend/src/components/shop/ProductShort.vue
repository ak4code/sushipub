<template>
    <div v-loading="loading">
        <div class="uk-flex uk-grid-small uk-grid-match uk-margin-bottom uk-child-width-1-1 uk-child-width-1-3@s uk-child-width-1-4@m uk-child-width-1-5@l"
             uk-grid v-if="products.length">
            <div v-for="product in products" :key="product.id">
                <product-card :product="product"></product-card>
            </div>
            <div v-if="category">
                <a :href="category.link"
                   class="uk-flex uk-flex-middle uk-text-large uk-text-center pub-product-cat-link">
                    <div class="uk-width-1-1">
                        Показать все
                        <br>
                        {{category.name}}
                    </div>
                </a>
            </div>
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
            ProductCard,

        },
        data: () => ({
            products: [],
            category: null,
            count: 0,
            loading: true
        }),
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products/short_list?category=${this.categoryId}&ordering=-price`)
                this.products = data
                await this.getCategory(data)
                this.loading = false
            },
            async getCategory (res) {
                if (res[0].hasOwnProperty('category_info')) this.category = res[0].category_info
            }
        }
    }
</script>

<style scoped>

</style>