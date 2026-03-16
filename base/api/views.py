from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Todo
from .serializers import TodoSerializer

# List all tasks
@api_view(['GET'])
def tasks_list(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

# Get a single task
@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    serializer = TodoSerializer(task)
    return Response(serializer.data)


@api_view(['GET'])
def completed_tasks(request):
    tasks = Todo.objects.filter(completed=True)
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)