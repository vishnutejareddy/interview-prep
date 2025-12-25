# Project Structure

## Root Organization
```
/
├── coding/           # Coding problems and algorithms
├── python/           # Python-specific interview content
├── system-design/    # System architecture and design
└── README.md         # Main project overview
```

## Coding Section (`/coding/`)
- **data-structures/**: Core data structures (arrays, trees, graphs, etc.)
- **algorithms/**: Algorithm implementations (sorting, searching, DP, etc.)  
- **patterns/**: Common problem-solving patterns (two pointers, sliding window, etc.)
- Each subsection has its own README.md with navigation links

## Python Section (`/python/`)
- **language-features/**: Python-specific constructs (decorators, generators, etc.)
- **libraries/**: Standard library modules relevant to interviews
- **best-practices/**: Code style, performance, and testing guidelines

## System Design Section (`/system-design/`)
- **fundamentals/**: Core concepts (scalability, consistency, CAP theorem)
- **components/**: System building blocks (databases, caches, load balancers)
- **case-studies/**: End-to-end system design examples

## File Naming Conventions
- Use lowercase with hyphens: `two-pointers.md`, `hash-tables.md`
- Descriptive names that match the concept being documented
- Consistent README.md files in each directory for navigation

## Content Structure Standards
Each topic file should include:
1. **Key Concepts**: Brief explanation of the topic
2. **Code Examples**: Python implementations with proper formatting
3. **Common Patterns**: Reusable approaches and templates
4. **Problems Solved**: Checklist of related practice problems
5. **Complexity Analysis**: Time and space complexity for each solution

## Navigation Pattern
- Root README links to main sections
- Section READMEs link to individual topics
- Cross-references between related concepts
- Progress tracking with checkboxes throughout