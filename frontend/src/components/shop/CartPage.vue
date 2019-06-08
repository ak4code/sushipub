<template>
    <div class="cart-page">
        <div class="uk-card uk-card-small uk-card-default uk-card-body">
            <div class="uk-padding">
                <el-steps :active="active" finish-status="success" align-center>
                    <el-step title="Корзина"></el-step>
                    <el-step title="Доставка"></el-step>
                    <el-step title="Готово"></el-step>
                </el-steps>
            </div>
            <div class="cart" v-if="active === 0">
                <el-table
                        :data="items"
                        border
                        style="width: 100%"
                        size="mini"
                        fit
                        show-header
                >
                    <el-table-column
                            type="index"
                            label="#"
                            width="50">
                    </el-table-column>
                    <el-table-column
                            width="100"
                            align="center"
                    >
                        <template slot-scope="scope">
                            <img class="uk-preserve-width uk-border-rounded" :src="scope.row.product.image" width="70"
                                 alt=""
                                 v-if="scope.row.product.image">
                            <img class="uk-preserve-width uk-border-rounded"
                                 src="/static/noimage.png"
                                 width="70"
                                 alt="" v-else>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="product.name"
                            label="Наименование">
                    </el-table-column>
                    <el-table-column
                            prop="product.price"
                            label="Цена"
                            width="80"
                            align="center"
                            suffix="р."
                    >
                    </el-table-column>
                    <el-table-column
                            label="Кол-во"
                            width="150"
                            align="center"
                    >
                        <template slot-scope="scope">
                            <el-input-number v-model="scope.row.qty" @change="handleChangeQty(scope.row)" :min="1"
                                             :max="20" size="mini"></el-input-number>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="Сумма"
                            width="80"
                            align="center"
                    >
                        <template slot-scope="scope">
                            {{scope.row.product.price * scope.row.qty}} р.
                        </template>
                    </el-table-column>
                    <el-table-column width="80" align="center">
                        <template slot-scope="scope">
                            <el-button size="mini" type="danger" icon="el-icon-delete"
                                       @click="deleteItemCart(scope.$index)" circle></el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <div class="uk-flex uk-flex-middle uk-flex-wrap uk-grid-small uk-padding uk-flex-between">
                    <div class="uk-margin-bottom">
                        <label class="uk-margin-small-right">Выберите район доставки</label>
                        <el-select v-model="formDelivery.area"
                                   placeholder="Доставка" @change="changeDelivery" name="delivery">
                            <el-option
                                    v-for="item in areas"
                                    :key="item.id"
                                    :label="item.name"
                                    :value="item.id">
                            </el-option>
                        </el-select>
                    </div>
                    <div class="uk-margin-bottom">
                        <el-button type="success" @click="next" :disabled="!formDelivery.area">
                            Оформить заказ
                        </el-button>
                    </div>
                    <div class="uk-flex-first uk-margin-bottom">
                        <div v-if="delivery">Доставка: + {{delivery}} руб.</div>
                        <div class="uk-text-large">Итого: {{total}} руб.</div>
                    </div>
                </div>
            </div>
            <div class="delivery" v-else-if="active === 1">
                <el-form ref="formDelivery" :model="formDelivery">
                    <el-form-item label="Ваше имя">
                        <el-input v-model="formDelivery.name" placeholder="Ваше имя">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Номер телефона">
                        <el-input v-model="formDelivery.phone" placeholder="+7 999 999-99-99">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Район доставки">
                        <el-select v-model="formDelivery.area"
                                   placeholder=" Доставка" @change="changeDelivery" disabled>
                            <el-option
                                    v-for="item in areas"
                                    :key="item.id"
                                    :label="item.name"
                                    :value="item.id">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Адрес">
                        <el-input v-model="formDelivery.address" placeholder="ул. Декабристов д. 9г">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Количество персон">
                        <el-input-number :min="1" :max="10" v-model="formDelivery.person" type="number">
                        </el-input-number>
                    </el-form-item>
                    <el-form-item label="Комментарий к заказу">
                        <el-input v-model="formDelivery.comment" type="textarea">
                        </el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="checkout('formDelivery')" v-loading="loading">Заказать</el-button>
                    </el-form-item>
                </el-form>
            </div>
            <div class="success" v-else-if="active >= 2">
                <div class="uk-flex uk-flex-middle uk-flex-center">
                    <div class="uk-margin uk-padding">
                        <div class="uk-card uk-padding-large uk-text-center uk-card-default uk-box-shadow-large">
                            <h2>Ваш заказ оформлен!</h2>
                            <div class="uk-text-large uk-margin">Ожидайте звонка оператора для потверждения заказа.</div>
                            <a href="/">
                                <el-button type="primary">На главную</el-button>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters, mapMutations} from 'vuex'

    export default {
        name: "cart-page",
        data: () => ({
            active: 0,
            tooltip: true,
            loading: false,
            areas: [],
            formDelivery: {
                name: null,
                phone: null,
                address: null,
                area: null,
                person: 1,
                comment: null
            }
        }),
        created () {
            this.getDestinations()
            this.getCart()
        },
        mounted () {
            document.getElementsByName('delivery')[0].focus()
        },
        computed: {
            ...mapGetters({
                items: 'getItems',
                total: 'getTotal',
                delivery: 'getDelivery',
            })
        },
        methods: {
            ...mapActions({
                getCart: 'getCartItems',
                changeItemCart: 'changeItemCart',
                deleteItemCart: 'deleteItemCart',
                resetCart: 'resetCart'
            }),
            ...mapMutations({
                setDelivery: 'SET_DELIVERY'
            }),
            changeDelivery () {
                let delivery = this.areas.find(i => i.id === this.formDelivery.area)
                this.setDelivery(this.total > 500 ? delivery.after : delivery.before)
            },
            async getDestinations () {
                await this.$axios.get('/api/destinations')
                    .then(res => this.areas = res.data)
                    .catch(e => console.log(e))
            },
            handleChangeQty (item) {
                this.changeItemCart(item)
            },
            next () {
                this.active++
            },
            async checkout (form) {
                this.loading = true
                let dForm = this.$refs[form].model
                let order = {
                    ...dForm,
                    items: this.items
                }
                await this.$axios.post('/api/orders/checkout', order)
                    .then(() => {
                        this.active = 2
                        this.resetCart()
                        this.loading = false
                        this.active++
                    })
                    .catch(e => console.dir(e))
            }
        }
    }
</script>

<style scoped>

</style>