var str='';
var xiang_str='';
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
	 	$('.html_title').html('');

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
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
			$('.show_data').html(str)
			$('.clear_padding').hide()
        }
    }else if(path_ajax=='1'){
        // 疾病信息
        obj_shumei['url']='/dev/search_disease/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(1,'+data["disease_id"]+')">'+data['disease_icd_cn']+'</div>';
				str_head=Number(index)+1;
        	});
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
			$('.show_data').html(str);
			$('.html_title').html('找到 \"'+val+'\" 相关结果'+str_head+'条')
        }
    }
	$.ajax({
		url:obj_shumei['url'],
		type:"POST",
		data:{name:val},
		success:obj_shumei.str_fun
	})
}
function get_xiangqign(id,list_id){
	xiang_str="";
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
			$('.yiyuan_xiang').slideDown(500);
			$('.search_yiyuan').hide(500);
		}
	}else if (id=='1') {
		// 疾病详情
		xiangqing['url']='/dev/search_disease_dict/';
		xiangqing['data']={disease_id:list_id};
		xiangqing['data_xiang']=function(msg){
			$.each(msg['data']['data'], function(index, data) {
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>'
				xiang_str+='<div class="text-left">【疾病名称】</div>';
				xiang_str+='<div class="text-left">'+data['disease_icd_cn']+'</div>';
				xiang_str+='<div class="text-left">【ICD编码】</div>';
				xiang_str+='<div class="text-left">'+data['disease_icd']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str)
			$('.yiyuan_xiang').slideDown(500);
			$('.search_yiyuan').slideUp(500);
		}
	}else if (id=='2') {
		// 药品详情
		xiangqing['url']='/dev/search_Drugs_dict/';
		xiangqing['data']={drug_id:list_id};
		xiangqing['data_xiang']=function(msg){
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
			$('.yiyuan_xiang').slideDown(500);
			$('.search_yiyuan').slideUp(500);
		}
	}
	$.ajax({
		url:xiangqing['url'],
		type:"POST",
		data:xiangqing['data'],
		success:xiangqing.data_xiang
	})
}
function hide_true(){
	$('.yiyuan_xiang').slideUp(500,function(){

	$('.search_yiyuan').show(100);
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
	$('.l_list').css({'left':'0px'})
	}
window.onresize=function(){
	var screenWidth=$(window).width();
	if(screenWidth>=768){
		$('.l_list').removeClass('l_list_screen');
		$('.l_list').css({'left':'0px'})
		console.log(121212)
	}else{
		console.log(10000000)
		$('.l_list').addClass('l_list_screen');
		$('.l_list').css({'left':'-210px'})
	}
}