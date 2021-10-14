import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {


        /*网络适配参数*/

        http_header:'http://',

        mock:'http://mock-api.com/VKyyO3Kw.mock/',
        // ip:'192.168.3.103:5000',
        // ip:'127.0.0.1:5000',
        ip:'100.68.246.17:5000',
        connection_test:'/',
        route_name_list:'/NameList',
        route_processed_data:'/ProcessedData',
        route_capacity:'/capacity',
        route_knee_point:'/knee_point',
        route_knee_degree:'/knee_degree',
        route_online_degree_all:'/online_degree_all',
        route_online_rank_all:'/online_rank_all',
        route_predicted_ctk:'/predicted_ctk',
        /**************************************************/

        /***  电池数据存储参数 ****/

        all_cell_data:1,
        single_cell:null,
        all_cell_evaluation:[],

        current_cell_name:'cccc',

        cell_name_list: 1,
        fig1_capacity:null,
        fig1_cycle:null,
        fig1_capacity_rate:[],
        normalized_capacity:null,
        normalized_cycle:null,

        knee_point:null,
        angle_degree:null,
        square_degree:null,

        online_degree:null,
        valid_length:null,

        online_rank:null,
        diff_cycle:null,

        predicted_ctk:null,
        true_ctk:null,

        IC_DV:null,
        IR:null,
        Qd_lin:null,
        V_lin:null,
        abs_IC_DV_max:null,
        abs_IC_DV_pos:null,

        current_capacity:[],
        aging_degree:[],



        /********************************临时调试数据****************************************/

        b1c4:1,
        b1c4_parameter:1,

        /**************************************************************************/




    },
    mutations: {


    },
    actions: {


    },
    modules: {

    }
})
