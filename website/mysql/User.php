<?php

/**
 * @filename User.php 
 * @encoding UTF-8 
 * @author hmj
 * @datetime 2017-3-2  
 * @version 1.0
 * @Description 用户的相关信息
 */
class User extends YF_Controller {

    //客户列表
    public function user_customer() {
        $this->header('直客列表');
        $this->load->model('adm_aduser_model');
        $data = $this->input->get();
        $data['source_from'] = isset($data['source_from'])?intval($data['source_from']):'-1';
		
        $where = $this->adm_aduser_model->parse_where(array_map('trim', $data));

        $this->load->model('Adm_seller_model','seller_model');
        $admin_id = $this->session->userdata['id'];
        if($this->session->userdata['roleid'] == 7){
            $pid_ary = array('10'=>1,'22'=>37,'21'=>42);
            $pid = $pid_ary[$admin_id];
            if($this->session->userdata['id'] == 8){
                $role_sel_where = $this->seller_model->get_many_by(array(),'id');
            }else{
                $role_sel_where = $this->seller_model->get_many_by(array('pid'=>$pid),'id');
            }
            $member = array_column($role_sel_where, 'id');
            
            $member_str =  explode(',', $pid.','.implode(',',$member));
            $where['membername'] = $member_str;
            if(!empty($data['sellers'])){
                if($this->session->userdata['id'] == 8){
                    $sql = "SELECT id FROM `wf_seller` WHERE name like '{$data['sellers']}%'";
                }else{
                    $sql = "SELECT id FROM `wf_seller` WHERE name like '{$data['sellers']}%' AND (pid = $pid OR id = $pid)";
                }
                $query = $this->db->query($sql);
                $sel_where = $query->result_array(); 
                if (empty($sel_where)) {
                    $where['membername'] = -1;
                }else{
                    $member = array_column($sel_where, 'id');
                    $where['membername'] = $member;
                }
            }
        }else{
            if(!empty($data['sellers'])){
                //得到满足条件的订单id
                $sel_where = $this->seller_model->get_by(array('name'=>$data['sellers']),'id');
                if(!empty($sel_where)){
                    $where['membername'] = $sel_where['id'];
                }else{
                    $where['membername'] = -1;
                }
            }
        }
        
        if(empty($data['nickname'])){
            $where['agent_id'] = array(1,100000);
        }
        
        $config['total_rows'] = $this->adm_aduser_model->count_by($where);
        $config['base_url'] = base_url('user/user_customer');
        $curpage = $this->uri->segment(3, 1);
        $this->load->library("pagination"); //载入
        $this->pagination->initialize($config);
        $limit = $this->pagination->per_page;
        $offset = ($curpage - 1) * $limit;
        $data['user_list'] = $this->adm_aduser_model->get_list('id,start_putnum,agent_id,oem_uid,nickname,phone,money,status,membername,add_time,in_money,source_from,source_wd,fromaddress', $where, array($limit, $offset), array('id', 'desc'));
        $this->load->model('oemuser_model');
        $site_name = $this->oemuser_model->get_many_by(array(),'id,site_name');
        $data['site_name'] = array_column($site_name, 'site_name','id');
        $this->load->model('product_model');
        $data['product'] = $this->product_model->get_many_by(array(), 'pid,product_name,aduser_price');
        
        $money = $this->adm_aduser_model->get_bys($where, 'sum(money) allmoney');
        
        $data['money'] = $money['allmoney'];
        $data['total_rows'] = $config['total_rows'];

        $this->load->model('adm_seller_model');
        $sellers = $this->adm_seller_model->get_many_by(array());
        $data['seller'] = array_column($sellers, 'name', 'id');
        $data['seller_nickname'] = array_column($sellers, 'nickname', 'id');
        
        $data['page'] = $this->pagination->create_links();
        $this->load->view('User/user_customer', $data);
    }

    //增删销售人员
    public function editSellerName() { 
        //新增销售功能人员功能
        $addSellerName = $this->input->post('addSellerName');//接收新增的销售人员
        $this->load->model('adm_seller_model');
        if ($addSellerName) {//如果有值就添加销售人员
            $pid = $this->input->post('pid');
            $str = trim($addSellerName,',');//去掉最后一位','
            $arr = explode(',',$str);
            foreach ($arr as $value) {
               $dataArr[] = array('name'=>$value,'pid'=>$pid);
            }
            $this->adm_seller_model->insert_many($dataArr);
        }

        //删除销售人员功能
        $delSellerName = $this->input->post('delSellerName');//接收删除的销售人员
        $up_deldata = array();
        if ($delSellerName) {//如果有值就添加销售人员
             $str = trim($delSellerName,',');//去掉最后一位','
             $arr = explode(',',$str);
             foreach ($arr as $value) {
                $up_deldata[] = array(
                    'id'=>$value,
                    'is_del'=>1
                );
            }
            if(!empty($up_deldata)){
                $this->adm_seller_model->update_batch($up_deldata,'id');
            }
        }
        exit;
    }


    public function customer_detail() {
        $this->header('广告用户详情');
        $userid = $this->uri->segment(3, 0);
        !empty($userid) or die();
        $this->load->model('adm_aduser_model');
        $data = $this->adm_aduser_model->get($userid, 'id,agent_id,nickname,phone,money,in_money,status,start_putnum,add_time,membername');
        if (empty($data)) {
            $this->error('当前的用户不存在');
        }
        $data['usertype'] = '直客';
        if ($data['agent_id'] > 1) {
            $this->load->model('agent_model');
            $agent = $this->agent_model->get($data['agent_id'], 'nickname');
            if (!empty($agent)) {
                $data['usertype'] = "{$agent['nickname']}的广告商";
            }
        }
        $this->load->model('adm_seller_model');
        $sellers = $this->adm_seller_model->get_many_by(array('is_del'=>'0'));
        $data['seller'] = array_column($sellers, 'name', 'id');
        $director = $this->adm_seller_model->get_many_by(array('pid'=>'0','is_del'=>'0'));
        $data['director'] = array_column($director, 'name', 'id');
        $this->load->view('User/customer_detail', $data);
    }

    public function reset_pwd() {
        $this->load->model('adm_aduser_model');
        $pwd = $this->input->post('passwd');
        $uid = $this->input->post('aduserid');
        $newpwd = password_hash($pwd, PASSWORD_DEFAULT);
        $this->adm_aduser_model->update($uid, array('password' => $newpwd));
        $this->success('更新成功');
    }

    public function user_edit() {
        $data = $this->input->post();
        $id = $data['aduserid'];
        unset($data['aduserid'], $data['passwd']);

        !empty($id) or $this->error('当前的用户不存在');
        $this->load->model('adm_aduser_model');
        $this->adm_aduser_model->update($id, $data);
        $this->success('更新成功', site_url('user/user_customer'));
    }

    public function customer_checker() {
        $this->load->model('aduser_model');
        $status = $this->input->post('status');
        $uid = $this->input->post('uid');
        $user = $this->aduser_model->get_aduser($uid);
        if (empty($user)) {
            $this->error('当前的用户不存在');
        }
        
        $this->aduser_model->up_aduser($uid, array('status' => $status, 'is_scan' => 1));
        $this->success('更新成功');
    }

    //代理商列表
    public function user_agent() {
        $this->header('代理商列表');
        $this->load->view('User/user_agent');
    }

    public function tmp_to_agent() {
        $uid = $this->input->post('uid');
        $agent_id = $this->input->post('agentid');
        $this->load->model('aduser_model');
        if (!in_array($agent_id, array('100000', '1'))) {
            exit;
        }
        $this->load->model('price_model');
        $this->price_model->delete_by(array('usertype' => 1, 'userid' => $uid));

        if ($agent_id === '100000') {
            $this->load->model('product_model');
            $product_ary = $this->product_model->get_many_by(array(), 'pid,agent_price');
            $price_ary = array();
            foreach ($product_ary as $product) {
                $pid = $product['pid'];
                $agent_price = $product['agent_price'];
                $price_ary[] = array(
                    'pid' => $pid,
                    'userid' => $uid,
                    'usertype' => 2,
                    'price' => $agent_price,
                    'add_time' => $_SERVER['REQUEST_TIME']
                );
            }
            $this->load->model('price_model');
            $this->price_model->insert_many($price_ary);
        }
        $this->aduser_model->update($uid, array('agent_id' => $agent_id));
        $this->success('更新成功');
    }

    public function ceshiceshi(){
        
//        $list = \think\Db::name('u')->select();
//        foreach ($list as $k => $v) {
//            $v['order_info'] = count(\think\Db::name('order')->where(['u_id' => $v['id']])->group('u_id')->select());
//            $arr[$v['yq']][] = $v;
//        }
//        $new_arr=[];
//         foreach ($arr as $k => &$val) {
//            $new_arr[$k]['reg_count'] = count($val);
//            $new_arr[$k]['order_count'] = array_sum(array_column($val, 'order_info'));
//            
//        }
        
        $sql = "SELECT id,source_from FROM `wf_aduser` WHERE add_time >= 1558281600 AND add_time <= 1558540800";
        $query = $this->db->query($sql);
        $result = $query->result_array();
        
        $this->load->model('Order_model','order_model');
        $arr = [];
        foreach($result as $k=>$v){
            $v['order_info'] = count($this->order_model->group_by('aduser_id')->get_by(array('aduser_id'=>$v['id']),'id'));
            $arr[$v['source_from']][] = $v;
        }
        $new_arr = [];
        $all_reg_count = $all_order_count = 0;
        foreach($arr as $k => &$val){
            $new_arr[$k]['reg_count'] = count($val);
            $new_arr[$k]['order_count'] = array_sum(array_column($val, 'order_info'));
            $all_reg_count += $new_arr[$k]['reg_count'];
            $all_order_count += $new_arr[$k]['order_count'];
        }
        $data['all_reg_count'] = $all_reg_count;
        $data['all_order_count'] = $all_order_count;
        $data['user_list'] = $new_arr;
        
        print_r($data);
    }
    
    
    //快速注册详情列表
    public function user_register() {
        $this->header('订单搜索统计');
        $data = $this->input->get();
        
        $where = array();
        if(!empty($data['start_time'])){
            $where['add_time >='] = $start_time = strtotime($data['start_time']);
        }else{
            $data['start_time'] = date('Y-m-01', time());
            $where['add_time >='] = $start_time = strtotime($data['start_time']);
        }
        if(!empty($data['end_time'])){
            $where['add_time <='] = $end_time = strtotime($data['end_time']);
        }else{
            $data['end_time'] = date('Y-m-d', time());
            $where['add_time <='] = $end_time = time()+64800;
        }
        
        $sql = "SELECT id,source_from FROM `wf_aduser` WHERE add_time >= $start_time AND add_time <= $end_time";
        $query = $this->db->query($sql);
        $result = $query->result_array();
        
        $this->load->model('Order_model','order_model');
        $arr = [];
        foreach($result as $k=>$v){
            $v['order_info'] = count($this->order_model->group_by('aduser_id')->get_by(array('aduser_id'=>$v['id']),'id'));
            $arr[$v['source_from']][] = $v;
        }
        $new_arr = [];
        $all_reg_count = $all_order_count = 0;
        foreach($arr as $k => &$val){
            $new_arr[$k]['reg_count'] = count($val);
            $new_arr[$k]['order_count'] = array_sum(array_column($val, 'order_info'));
            $all_reg_count += $new_arr[$k]['reg_count'];
            $all_order_count += $new_arr[$k]['order_count'];
        }
        $data['all_reg_count'] = $all_reg_count;
        $data['all_order_count'] = $all_order_count;
        $data['user_list'] = $new_arr;

        $this->load->view('User/user_register',$data);
    }
    //快速注册详情列表
    public function order_info() {
        $this->header('订单详情');
        $data = $this->input->get();
        
        $type = $data['type'];
        if(!empty($data['start_time'])){
            $start_time = strtotime($data['start_time']);
        }else{
            $data['start_time'] = date('Y-m-01', time());
            $start_time = strtotime(date('Y-m-01', time()));
        }
        if(!empty($data['end_time'])){
            $end_time = strtotime($data['end_time'])+64800;
        }else{
            $data['end_time'] = date('Y-m-d', time());
            $end_time = time()+64800;
        }
//        opcache_reset();
//        $sql = "SELECT a.source_from source_from,o.id,o.wechat_name,a.source_wd FROM `wf_order` o LEFT JOIN `wf_aduser` a ON o.aduser_id = a.id WHERE a.add_time >= $start_time AND a.add_time <= $end_time AND a.source_from = $type";
        $sql = "SELECT a.source_from source_from,o.id,o.wechat_name,a.source_wd,o.price FROM `wf_order` o LEFT JOIN `wf_aduser` a ON o.aduser_id = a.id WHERE a.add_time >= $start_time AND a.add_time <= $end_time AND a.source_from = $type group by o.aduser_id";
        $query = $this->db->query($sql);
        $data['order'] = $query->result_array();
        
        $all_sql = "SELECT SUM(o.price*o.need_fans) money FROM `wf_order` o LEFT JOIN `wf_aduser` a ON o.aduser_id = a.id WHERE a.add_time >= $start_time AND a.add_time <= $end_time AND a.source_from = $type";
        $all_query = $this->db->query($all_sql);
        $data['all_money'] = $all_query->result_array();
        
        $this->load->view('User/order_info',$data);
    }
    public function user_keyword() {
        $this->header('注册搜索统计');
        $data = $this->input->get();
        
        $where = array();
        if(!empty($data['start_time'])){
            $where['add_time >='] = $start_time = strtotime($data['start_time']);
        }else{
            $data['start_time'] = date('Y-m-01', time());
            $where['add_time >='] = $start_time = strtotime(date('Y-m-01', time()));
        }
        if(!empty($data['end_time'])){
            $where['add_time <='] = $end_time = strtotime($data['end_time']);
        }else{
            $data['end_time'] = date('Y-m-d', time());
            $where['add_time <='] = $end_time = time()+64800;
        }
        
        $this->load->model('adm_aduser_model','user_model');
        $config['total_rows'] = $this->user_model->group_by('source_from,source_wd')->count_by($where);
        $config['base_url'] = base_url('user/user_keyword');
        $curpage = $this->uri->segment(3, 1);
        $this->load->library("pagination"); //载入
        $this->pagination->initialize($config);
        $limit = $this->pagination->per_page;
        $offset = ($curpage - 1) * $limit;
        $data['user_list'] = $this->user_model->group_by('source_from,source_wd')->get_list('count(*) all_num,source_from,source_wd', $where, array($limit, $offset), array('all_num', 'desc'));
        $data['page'] = $this->pagination->create_links();
        $data['total_rows'] = $config['total_rows'];
        
        $data['all_user'] = $this->user_model->get_many_by($where,'count(*) all_num');
        $this->load->view('User/user_keyword',$data);
    }
    
    //添加直客
    public function user_add(){
        $data = $this->input->post();
        !empty($data['nickname']) or $this->error('公司名称不能为空');
        !empty($data['phone']) or $this->error('联系电话不能为空');
        $this->load->model('adm_aduser_model','aduser_model');
        $aduser = $this->aduser_model->get_by(array('phone'=>$data['phone'],'oem_uid'=>1,'oem_id'=>1));
        if(!empty($aduser)){
            $this->error('已存在该用户');
        }
        $data['password'] = password_hash('123456', PASSWORD_DEFAULT);
        $data['add_time'] = time();
        $add_user = $this->aduser_model->insert($data);
        if($add_user){
            $this->success('添加成功');
        }else{
            $this->error('执行有误');
        }
        
    }
    
    //退款用户统计
    public function show_user_info(){
        $userid = $this->input->post('userid');
        if(empty($userid)){
            $this->success(array('nickname'=>'','phone'=>'','money'=>''));
        }
        $this->load->model('aduser_model');
        $userinfo = $this->aduser_model->get($userid);
        if(empty($userinfo)){
            $this->error('当前的信息有误');
        }
        $userinfo['userid'] = $userid;
        $this->success($userinfo);
    }
    
    //退款操作
    public function return_money(){
        $data = $this->input->post();
        $userid = $data['userid'];
        $change_money = $data['change_money'];
        empty($userid) && $this->error('该用户不存在');
        $this->load->model('aduser_model');
        $user = $this->aduser_model->get_by(array('id'=>$userid),'money');
        if($user['money'] < $change_money){
            $this->error('账户余额不足，退款失败');
        }
        $money = $user['money']-$change_money;
        $this->aduser_model->update_by(array('id'=>$userid),array('money'=>$money));
        $this->load->model('Adm_clientfinance_model', 'clientfinance');  //客户金额明细
        $clientfinance = array(
            'money' => $money,
            'charge_money' => $change_money,
            'status' => 4,
            'money_type' => 2,
            'userid' => $userid,
            'usertype' => 1,
            'remark' => "客户退款至手中".$change_money."元，账户余额".$money."元",
            'add_time' => $_SERVER['REQUEST_TIME']
        );
        $this->clientfinance->insert($clientfinance);  //客户金额明细
        $this->success("退款成功");
    }

}
