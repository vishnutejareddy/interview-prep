# Technology Stack

## Primary Language
**Python 3** - All code examples and solutions use Python for consistency and interview relevance.

## Documentation Format
- **Markdown** (.md files) for all documentation
- Structured with clear headings and code blocks
- Consistent formatting across all sections

## Code Standards
- Include docstrings with problem description, approach, time/space complexity
- Use descriptive variable names
- Follow Python naming conventions (snake_case)
- Include test cases with assertions
- Add complexity analysis comments

## Required Code Template
```python
def solution(input_data):
    """
    Problem: [Brief description]
    
    Approach: [Algorithm/pattern used]
    Time: O(?)
    Space: O(?)
    """
    pass

# Test cases
assert solution(test_input) == expected_output
```

## Common Libraries
- `collections`: defaultdict, Counter, deque
- `heapq`: heappush, heappop for priority queues
- `bisect`: binary search operations
- Standard library only (no external dependencies)

## Build/Test Commands
This is a documentation-only repository with no build system. Code validation is done through:
- Manual testing with assert statements
- Python syntax checking: `python -m py_compile filename.py`
- Code review for correctness and style

## File Organization
- Use lowercase with hyphens for file names
- Group related content in appropriate subdirectories
- Maintain consistent README.md structure in each folder