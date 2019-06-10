<template>
    <div class="pub-category-detail">
        <div v-if="products.hasOwnProperty('count') && products.count !== 0">
            <div class="uk-flex uk-grid-small uk-grid-match uk-margin-small-bottom uk-child-width-1-1 uk-child-width-1-3@s uk-child-width-1-4@m uk-child-width-1-5@l"
                 uk-grid>
                <div v-for="product in products.results" :key="product.id">
                    <product-card :product="product"></product-card>
                </div>
            </div>
            <br>
            <div class="uk-flex uk-flex-center uk-margin" v-if="products.next">
                <div>
                    <el-button @click="loadMore" class="uk-button uk-button-default">Показать еще</el-button>
                </div>
            </div>
        </div>
        <div v-else>
            <div class="uk-flex uk-flex-center uk-padding-large"
                 v-loading="loading"
                 element-loading-text="Загрузка..."
                 element-loading-spinner="el-icon-loading"
                 element-loading-background="rgba(0, 0, 0, 0.8)"
                 style="min-height: 250px"
            >
                <div class="uk-text-center" v-if="!loading">
                    <h2 class="uk-text-center">Раздел еще не заполнен</h2>
                    <a href="/" class="uk-button uk-button-default">Вернуться на главную</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductCard from '@/components/shop/ProductCard'

    export default {
        name: "category-detail",
        props: {
            categoryId: {
                type: Number,
                required: true
            }
        },
        data: () => ({
            category: null,
            loading: true,
            products: {},
        }),
        components: {
            ProductCard
        },
        created () {
            this.getProducts()
        },
        mounted () {
            this.subscribe()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products?category=${this.categoryId}&ordering=-price`)
                this.products = data
                await this.getCategory(data.results)
                this.loading = false
            },
            async getCategory (res) {
                if (res.length) {
                    if (res[0].hasOwnProperty('category_info')) this.category = await res[0].category_info
                }
            },
            async loadMore () {
                await this.$axios.get(this.products.next)
                    .then(res => {
                        this.products.results.push(...res.data.results)
                        this.products.next = res.data.next
                        this.products.previous = res.data.previous
                    })
                    .catch()
            },
            subscribe () {
                const channel = this.$pusher.subscribe('order')

                channel.bind('checkout', function (data) {
                    console.log(data)
                }, this)
            }
        }
    }
</script>

<style scoped>

</style>