
# forms.py
class SomeModelForm(forms.ModelForm):
		# ModelForm 생성자 재정의
		# user 인자 추가 -> 추후 ModelForm 호출시 첫번째 인자로 넘길 값을 받을 변수
    def __init__(self, user, *args, **kwargs):
				# 부모의 ModelForm의 생성자 실행
        super(SomeModelForm, self).__init__(*args, **kwargs)
				# 1:N 관계를 맺을 필드 재정의
				# 필드에 노출될 queryset을 ModelForm 호출시 넘겨준 `user`를 기반으로 참조 대상 조회
        self.fields['RelationModelFieldname'].queryset = RelationModel.objects.filter(user=user)
        
    class Meta:
        model = SomeModelForm
        fields = '__all__'

# views.py
def some_model_create(request):
    if request.method == 'POST':
				# 데이터 저장시에는 request.POST에 담긴 값으로 저장하지만,
				# ModelForm의 첫 번째 인자로 user를 받기로 하였으므로 첫번째 인자를 작성
        form = SomeModelForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps:view_name')
    else:
				# 첫번째 인자 user 정보 입력
        form = SomeModelForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'apps/some_model_create.html', context)
                                