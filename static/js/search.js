var str='';
var xiang_str='';
var title="";
var str_head='';
var obj_shumei={};
var xiangqing={};
	$('.center_content').click(show_list);
	function show_list(){
		var index=$(this).attr('data-type');
		$(this)
			.parent('.left_list')
			.find('.center_content')
			.addClass('style_list')
			.parent('.left_list')
			.siblings()
			.find('.center_content')
			.removeClass('style_list');
		$('.r_list')
	 		.eq(index)
	 		.addClass('show')
	 		.siblings()
	 		.removeClass('show');
	 	hide_true();
	 	$('.l_list_screen').animate({'left':'-210px'},500)
	 	$('.form-control').val('');
	 	$('.show_data').html('');
	 	$('.html_title').html('热门搜索');

	}
function search_click(ele,number){
	var input_val=$(ele).siblings('.input_center').find('input').val();
	set_ajax(input_val,number)
}

function set_ajax(val,path_ajax){
	str = '';
	str_head='';
	if(path_ajax=='0'){
        // 医院信息
        obj_shumei['url']='/dev/search_hospital/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(0,'+data["hospital_idx_id"]+')">'+data['test_hospital_name']+'</div>'
        		str_head=Number(index)+1
        	});
        	if(str_head==''){
        		str_head=0;
        	}
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
			$('.show_data').html(str)
			$('.clear_padding').hide()
        }
    }else if(path_ajax=='1'){
        // 疾病信息
        obj_shumei['url']='/dev/search_disease/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(1,'+data["disease_id"]+')">'+data['disease_name']+'</div>';
				str_head=Number(index)+1;
        	});
        	if(str_head==''){
        		str_head=0;
        	}
			$('.show_data').html(str);
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
        }
    }else if(path_ajax=='2'){
        // 药品信息
        obj_shumei['url']='/dev/search_Drugs_alias/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(2,'+data["drug_id"]+')">'+data['drug_common_name']+'</div>';
				str_head=Number(index)+1;
        	});
        	if(str_head==''){
        		str_head=0;
        	}
			$('.show_data').html(str);
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
        }
    }else if(path_ajax=='3'){
        //检验检查指标
        obj_shumei['url']='/dev/search_medical_alias/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(3,'+data["test_idx_id"]+')">'+data['test_idx_name']+'</div>';
				str_head=Number(index)+1;
        	});
        	if(str_head==''){
        		str_head=0;
        	}
			$('.show_data').html(str);
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
        }
    }
	$.ajax({
		url:obj_shumei['url'],
		type:"POST",
		data:{name:val},
		cache:false,
		success:obj_shumei.str_fun
	})
}
function get_xiangqign(id,list_id){
	xiang_str="";
	if(list_id==null){
		return;
	}
	if(id=='0'){
		// 医院详情
		xiangqing['url']='/dev/search_hospital_dict/';
		xiangqing['data']={hospital_idx_id:list_id};
		xiangqing['data_xiang']=function(msg){
			$.each(msg['data']['data'], function(index, data) {
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>'
				xiang_str+='<div class="text-left">【医院名称】</div>';
				xiang_str+='<div class="text-left">'+data['hospital_name']+'</div>';
				xiang_str+='<div class="text-left">【等级】</div>';
				xiang_str+='<div class="text-left">'+data['hospital_level']+'</div>';
				xiang_str+='<div class="text-left">【联系电话】</div>';
				xiang_str+='<div class="text-left">'+data['hospital_phone']+'</div>';
				xiang_str+='<div class="text-left">【地址】</div>';
				xiang_str+='<div class="text-left">'+data['hospital_address']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str)
			$('.yiyuan_xiang').slideDown(200);
			$('.search_yiyuan').hide(200);
		}
	}else if (id=='1') {
		// 疾病详情
		xiangqing['url']='/dev/search_disease_dict/';
		xiangqing['data']={disease_id:list_id};
		xiangqing['data_xiang']=function(msg){
			$.each(msg['data']['data'], function(index, data) {
				var drugs=data['drug_name'].split(' ');
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>'
				xiang_str+='<div class="text-left">【疾病名称】</div>';
				xiang_str+='<div class="text-left">'+data['disease_name']+'</div>';
				xiang_str+='<div class="text-left">【疾病描述】</div>';
				xiang_str+='<div class="text-left">'+data['disease_summary']+'</div>';
				xiang_str+='<div class="text-left">【就诊科室】</div>';
				xiang_str+='<div class="text-left">'+data['department_name']+'</div>';
				xiang_str+='<div class="text-left">【症状】</div>';
				xiang_str+='<div class="text-left">'+data['symptom_name']+'</div>';
				xiang_str+='<div class="text-left">【易感人群】</div>';
				xiang_str+='<div class="text-left">'+data['mode_of_infection']+'</div>';
				xiang_str+='<div class="text-left">【感染方式】</div>';
				xiang_str+='<div class="text-left">'+data['susceptible_population']+'</div>';
				xiang_str+='<div class="text-left">【治疗方式】</div>';
				xiang_str+='<div class="text-left">'+data['therapy_name']+'</div>';
				xiang_str+='<div class="text-left">【药物名称】<span style="font-size:12px;color:#999;">*点击获取药品详情*</span></div>';
				$.each(drugs,function(index100,data100){
					xiang_str+='<div class="text-left" onclick="getDrug(this)">'+data100+'</div>'
				})
				xiang_str+='<div class="text-left">【相关疾病】</div>';
				xiang_str+='<div class="text-left">'+data['about_disease_name']+'</div>';
				xiang_str+='<div class="text-left">【检查】</div>';
				xiang_str+='<div class="text-left">'+data['inspect_name']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str)
			$('.yiyuan_xiang').slideDown(200);
			$('.search_yiyuan').slideUp(200);
		}
	}else if (id=='2') {
		// 药品详情
		xiangqing['url']='/dev/search_Drugs_dict/';
		xiangqing['data']={drug_id:list_id};
		xiangqing['data_xiang']=function(msg){
			if(msg['data']['data']==''){
				$('.yiyuan_xiang').html('找不到该药品的详细信息！');
				$('.yiyuan_xiang').slideDown(200);
				$('.search_yiyuan').slideUp(200);
				return;
			}
			$.each(msg['data']['data'], function(index, data) {
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>';
				xiang_str+='<div class="text-left">【药品名称】</div>';
				xiang_str+='<div class="text-left">'+data['commonname']+'</div>';
				xiang_str+='<div class="text-left">【药品成分】</div>';
				xiang_str+='<div class="text-left">'+data['component']+'</div>';
				xiang_str+='<div class="text-left">【适用症状】</div>';
				xiang_str+='<div class="text-left">'+data['indication']+'</div>';
				xiang_str+='<div class="text-left">【用法用量】</div>';
				xiang_str+='<div class="text-left">'+data['dosage']+'</div>';
				xiang_str+='<div class="text-left">【药物作用】</div>';
				xiang_str+='<div class="text-left">'+data['drugInteractions']+'</div>';
				xiang_str+='<div class="text-left">【禁忌】</div>';
				xiang_str+='<div class="text-left">'+data['contraindications']+'</div>';
				xiang_str+='<div class="text-left">【不良反应】</div>';
				xiang_str+='<div class="text-left">'+data['adverseReactions']+'</div>';
				xiang_str+='<div class="text-left">【注意事项】</div>';
				xiang_str+='<div class="text-left">'+data['precautions']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str);
			$('.yiyuan_xiang').slideDown(200);
			$('.search_yiyuan').slideUp(200);
		}
	}else if (id=='3') {
		// 检查检验详情
		xiangqing['url']='/dev/search_medical_dict/';
		xiangqing['data']={id:list_id};
		xiangqing['data_xiang']=function(msg){
			$.each(msg['data']['data'], function(index, data) {
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>';
				xiang_str+='<div class="text-left">【指标名称】</div>';
				xiang_str+='<div class="text-left">'+data['test_idx_name']+'</div>';
				xiang_str+='<div class="text-left">【检验原理】</div>';
				xiang_str+='<div class="text-left">'+data['testprinciple']+'</div>';
				xiang_str+='<div class="text-left">【摘要】</div>';
				xiang_str+='<div class="text-left">'+data['summary']+'</div>';
				xiang_str+='<div class="text-left">【关联疾病】</div>';
				xiang_str+='<div class="text-left">'+data['diseaserelated']+'</div>';
				xiang_str+='<div class="text-left">【参考值】</div>';
				xiang_str+='<div class="text-left">'+data['normalvaluedescription']+'</div>';
				xiang_str+='<div class="text-left">【检验描述】</div>';
				xiang_str+='<div class="text-left">'+data['testdescription']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str);
			$('.yiyuan_xiang').slideDown(200);
			$('.search_yiyuan').slideUp(200);
		}
	}
	$.ajax({
		url:xiangqing['url'],
		type:"POST",
		data:xiangqing['data'],
		success:xiangqing.data_xiang
	})
}
function getDrug(ele){
	str="";
	title="";
	var keyword_drug=$(ele).text();
	$.ajax({
		url:'/dev/search_Drugs_alias/',
		data:{name:keyword_drug},
		type:"POST",
		success:function(data){
			if(data['data']['data']==''){
				return;
			}
			$.each(data['data']['data'], function(index, data) {
				title='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>';
				str+='<div class="text-left" style="clear:top;padding:15px 0px;" onclick="get_xiangqign(2,'+data["drug_id"]+')">'+data['drug_common_name']+'</div>';	
        	});
        	$('.yiyuan_xiang').html(title+str);
		}
	})	
}

function hide_true(){
	$('.yiyuan_xiang').slideUp(200,function(){

	$('.search_yiyuan').show();
	});
}
function click_val(ele){
	var text_val=$(ele).text()
	$('.form-control').val(text_val);
	set_ajax(text_val,0)
}
function samll_click(){
	$('.l_list_screen').animate({'left':'0px'},'500')
}
var screenWidth=$(window).width();
if(screenWidth>=768){
	$('.l_list').removeClass('l_list_screen')
	$('.l_list').css({'left':'0px'});
	$('.switch_img').attr('src','');
	}
window.onresize=function(){
	var screenWidth=$(window).width();
	if(screenWidth>=768){
		$('.l_list').removeClass('l_list_screen');
		$('.l_list').css({'left':'0px'})
		$('.switch_img').attr('src','');
	}else{
		$('.l_list').addClass('l_list_screen');
		$('.l_list').css({'left':'-210px'})
		$('.switch_img').attr('src','/static/img/tab_list.png');
	}
}