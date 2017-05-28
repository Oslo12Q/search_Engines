var str='';
var xiang_str='';
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
	}
function search_click(ele,number){
	var input_val=$(ele).siblings('.input_center').find('input').val();
	set_ajax(input_val,number)
}
function set_ajax(val,path_ajax){
	str = '';
	if(path_ajax=='0'){
        // 医院搜索
        obj_shumei['url']='/dev/search_hospital/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(0,'+data["hospital_idx_id"]+')">'+data['test_hospital_name']+'</div>';
        	});
        	// $('._scroll').before('<div class="col-sm-12 text-left" style="border-bottom:1px solid #f0f0f0;padding:0px 5px;">查询结果</div>');
			$('._scroll').html(str)
        }
    }else if(path_ajax=='1'){
        // 疾病搜索
        obj_shumei['url']='/dev/search_disease/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(1,'+data["disease_id"]+')">'+data['disease_icd_cn']+'</div>';
        	});
        	// $('._scroll').before('<div class="col-sm-12 text-left" style="border-bottom:1px solid #f0f0f0;padding:0px 5px;">查询结果</div>');
			$('._scroll').html(str)
        }
    }else if(path_ajax=='2'){
        // 药品搜索
        obj_shumei['url']='/dev/search_Drugs_alias/';
        obj_shumei['str_fun']=function(msg){
        	$.each(msg['data']['data'], function(index, data) {
				str+='<div class="text-left yiyuan_style" onclick="get_xiangqign(2,'+data["drug_id"]+')">'+data['drug_common_name']+'</div>';
        	});
        	// $('._scroll').before('<div class="col-sm-12 text-left" style="border-bottom:1px solid #f0f0f0;padding:0px 5px;">查询结果</div>');
			$('._scroll').html(str)
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
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>';
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
			$('.search_yiyuan').slideUp(500);
		}
	}else if (id=='1') {
		// 疾病详情
		xiangqing['url']='/dev/search_disease_dict/';
		xiangqing['data']={disease_id:list_id};
		xiangqing['data_xiang']=function(msg){
			$.each(msg['data']['data'], function(index, data) {
				xiang_str+='<span class="span_float" onclick="hide_true()" title="关闭">关闭</span>';
				xiang_str+='<div class="text-left">【疾病名称】</div>';
				xiang_str+='<div class="text-left">'+data['disease_icd_cn']+'</div>';
				xiang_str+='<div class="text-left">【ICD编码】</div>';
				xiang_str+='<div class="text-left">'+data['disease_icd']+'</div>';
        	});
			$('.yiyuan_xiang').html(xiang_str);
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
				xiang_str+='<div class="text-left">'+data['drug_common_name']+'</div>';
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
	$('.yiyuan_xiang').slideUp(500);
	$('.search_yiyuan').show(200);
}
function click_val(ele){
	var text_val=$(ele).text()
	$('.form-control').val(text_val);
	set_ajax(text_val,0)
}